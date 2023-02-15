import { ChangeDetectionStrategy, Component } from '@angular/core';
import { BehaviorSubject, combineLatest, of } from 'rxjs';
import {
  tap,
  map,
  startWith,
  distinctUntilChanged,
  share,
  withLatestFrom,
  take,
} from 'rxjs/operators';
import { ConditionalParserService } from '../services/conditional-parser.service';
import { SurveysService } from '../services/surveys.service';
@Component({
  changeDetection: ChangeDetectionStrategy.OnPush,
  selector: 'app-single-survey',
  template: `

  <app-survey-intro/>

    <pre>
    {{$any(filteredQuestions$ | async).length | json}}
  </pre>

    <section class="bg-light">
    <div class="container pt-3 pt-md-2 pt-md-5 pb-0">
      <div class="tw-flex">
        <div class="tw-w-1/12 tw-relative">
          <app-progress-bar [progress]="$any(currentProgress$ | async)"/>
        </div>
        <div class="tw-w-11/12">
        <app-question-list [answers]="$any(surveyAnswers$ | async)" (questionAnswered)="answerQuestion($event)" [questions]="questions"/>
        </div>
      </div>
    </div>
  </section>



  <section *ngIf="(currentProgress$ | async) === '100%'" class="bg-light">
    <div class="container">
      <div class="row">
        <div class="col">
          <div class="tw-flex tw-justify-end">
            <button
              (click)="handleSubmit()"     
              class="btn btn-primary d-block tw-w-32"
            >
              Terminer
            </button>
          </div>
        </div>
      </div>
    </div>
  </section>
  <app-survey-footer/>
  `,
  styles: [],
})
export class SingleSurveyComponent {
  surveyAnswers$ = new BehaviorSubject<Record<string, string | null>>({});
  conditions$ = new BehaviorSubject<Record<string, string | null>>({});

  questions: any[] = [];

  constructor(private surveysService: SurveysService) {}

  demoQuestions$ = this.surveysService.getDemoQuestions().pipe(
    tap((questions) => {
      this.questions = questions;
      const surveyAnswers: Record<string, null> = {};
      const conditions: Record<string, string | null> = {};
      questions.forEach((question) => {
        surveyAnswers[question.question_id] = null;
        if (question.condition) {
          conditions[question.question_id] = question.condition;
        }
      });
      this.surveyAnswers$.next(surveyAnswers);
      this.conditions$.next(conditions);
    }),
    share()
  );

  filteredQuestions$ = combineLatest([
    this.demoQuestions$,
    this.conditions$,
    this.surveyAnswers$,
  ]).pipe(
    tap((data) => {
      console.log(data[0]);
      console.log(data[1]);
      console.log(data[2]);
    }),
    map(([questions, conditions, surveyAnswers]) => {
      return questions.filter((question) =>
        this.checkIfSingleQuestionShouldBeDisplayed(
          question,
          conditions,
          surveyAnswers,
          questions
        )
      );
    }),
    tap((data) => {
      console.log(data);
    })
  );

  currentProgress$ = combineLatest([
    this.surveyAnswers$,
    this.conditions$,
  ]).pipe(
    distinctUntilChanged(),
    tap((data) => {
      console.log(data);
    }),
    map(([answers, conditions]) => {
      const numberOfQuestions = Object.values(answers).length;

      if (numberOfQuestions === 0) return 0;

      return (
        +(
          (Object.values(answers).filter((answer) => answer !== null).length /
            numberOfQuestions) *
          100
        ).toFixed(0) + '%'
      );
    }),
    share()
  );

  ngAfterViewInit() {
    this.demoQuestions$.subscribe(() => console.log('subbed'));
  }

  handleSubmit() {
    this.surveyAnswers$.pipe(take(1)).subscribe((answers) => {
      this.surveysService.demoSubmitAnswer(answers).subscribe((res) => {
        // TODO (jeremie + simon) this should be json with code, client should handle the message
        if (res) {
          alert(res);
        }
      });
    });
  }

  answerQuestion({
    questionId,
    questionAnswer,
  }: {
    questionId: string;
    questionAnswer: string;
  }) {
    of(null)
      .pipe(withLatestFrom(this.surveyAnswers$))
      .subscribe(([_, answers]) => {
        this.surveyAnswers$.next({
          ...answers,
          [questionId]: questionAnswer,
        });
      });
    return;
  }

  private checkIfSingleQuestionShouldBeDisplayed = (
    question: any,
    conditions: any,
    surveyAnswers: any,
    questions: any[]
  ) => {
    if (!question.condition) return true;

    const [questionID, operator, conditionAnswer] = this.parseCondition(
      question.condition
    );

    const conditionQuestion = questions.find(
      (question) => question.question_id === questionID
    );

    if (!conditionQuestion) return true;

    const currentAnswerForQuestion = surveyAnswers[question.question_id];
    const answerToBeat = surveyAnswers[questionID];

    if (answerToBeat === null) return false;

    switch (operator) {
      case '>':
        return +currentAnswerForQuestion > +conditionAnswer;

      case '<':
        return +currentAnswerForQuestion < +conditionAnswer;

      case '=':
        if (
          /,/.test(currentAnswerForQuestion)
            ? currentAnswerForQuestion
                .split(',')
                .includes(conditionAnswer.toString())
            : +currentAnswerForQuestion === +conditionAnswer
        ) {
          return true;
        } else {
          return false;
        }

      case '>=':
        return +currentAnswerForQuestion >= +conditionAnswer;

      case '<=':
        return +currentAnswerForQuestion <= +conditionAnswer;

      default:
        throw new Error('Unknown operator');
    }
  };
  parseCondition(condition: string): [string, string, number] {
    if (!condition) {
      throw new Error('No condition provided');
    }

    if (typeof condition !== 'string') {
      throw new Error('Condition must be a string');
    }

    const conditionalOperators: string[] = [];

    // todo cleanup this part
    for (let i = 0; i < condition.length; i++) {
      if (
        i < condition.length &&
        condition[i] === '>' &&
        condition[i + 1] === '='
      ) {
        conditionalOperators.push('>=');
        i++;
        continue;
      }
      if (
        i < condition.length &&
        condition[i] === '<' &&
        condition[i + 1] === '='
      ) {
        conditionalOperators.push('<=');
        i++;
        continue;
      }
      if (condition[i] === '>') {
        conditionalOperators.push('>');
        continue;
      }

      if (condition[i] === '<') {
        conditionalOperators.push('<');
        continue;
      }

      if (condition[i] === '=') {
        conditionalOperators.push('=');
        continue;
      }
    }

    // const conditionalOperators = condition.match(/>|<|>=|<=|=/g);

    if (!conditionalOperators || conditionalOperators.length == 0) {
      throw new Error(
        "condition argument must contain '>', '<', '>=', '<=' or '='"
      );
    }

    if (conditionalOperators.length > 1) {
      console.error(condition);
      throw new Error(
        'condition argument must contain exactly one of ">", "<", ">=", "<=" or "="'
      );
    }

    const conditionalOperator = conditionalOperators[0] as string;

    const [questionId, numberToCompare] = condition.split(
      new RegExp(conditionalOperator)
    );

    if (!questionId) {
      console.error(condition);
      throw new Error('questionId must be defined');
    }

    if (!numberToCompare) {
      console.error(condition);
      throw new Error('numberToCompare must be defined');
    }

    // https://regex101.com/

    if (!/^\d+(\.\d+)?$/.test(numberToCompare)) {
      console.error(condition);
      throw new Error(
        'numberToCompare must be a number in the standard decimal format (At least one number, followed by an optional group starting with one dot and 1 or more numbers. Ex : 5, 1.1, 1.05)'
      );
    }

    return [questionId, conditionalOperator, +numberToCompare];
  }
}
