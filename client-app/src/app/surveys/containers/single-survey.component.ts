
import { ChangeDetectionStrategy, Component } from '@angular/core';
import { BehaviorSubject } from 'rxjs';
import { tap, map, startWith } from 'rxjs/operators';
import { SurveysService } from '../services/surveys.service';
@Component({
  changeDetection: ChangeDetectionStrategy.OnPush,
  selector: 'app-single-survey',
  template: `

  <app-survey-intro/>
    <section class="bg-light">
    <div class="container pt-3 pt-md-2 pt-md-5 pb-0">
      <div class="tw-flex">
        <div class="tw-w-1/12 tw-relative">
          <app-progress-bar [progress]="$any(currentProgress$ | async)"/>
        </div>
        <div class="tw-w-11/12">
        <app-question-list [answers]="surveyAnswers" (questionAnswered)="answerQuestion($event)" [questions$]="demoQuestions$"/>
        </div>
      </div>
    </div>
  </section>

  

  <section class="bg-light">
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
  styles: [
  ]
})
export class SingleSurveyComponent {

  surveyAnswers: Record<string, string | null> = {};

  demoQuestions$ = this.surveysService.getDemoQuestions().pipe(tap(questions => {
    questions.forEach(question => {
      this.surveyAnswers[question.question_id] = null;
      this.numberOfQuestions++;
    })

  }))

  progressPercent$ = new BehaviorSubject<number>(0);

  numberOfQuestions = 0;

  currentProgress$ = this.progressPercent$.asObservable().pipe(
    map(percent => {
      return percent + "%"
    })
  )




  constructor(private surveysService: SurveysService) { }


  handleSubmit() {
    this.surveysService.demoSubmitAnswer(this.surveyAnswers).subscribe(res => {
      // TODO (jeremie + simon) this should be json with code, client should handle the message
      if (res) {
        alert(res)
      }
    })
  }


  answerQuestion({ questionId, questionAnswer }: { questionId: string; questionAnswer: string }) {
    this.surveyAnswers[questionId] = questionAnswer;

    this.trackProgress()
  }

  private trackProgress() {

    const percentDone = this.computePercentDone()

    this.progressPercent$.next(percentDone)
  }


  private computePercentDone() {

    if (this.numberOfQuestions === 0) return 0;

    return +((Object.values(this.surveyAnswers).filter(answer => answer !== null).length / this.numberOfQuestions) * 100).toFixed(0)

  }



}


