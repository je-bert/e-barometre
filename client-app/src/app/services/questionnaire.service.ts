import { Injectable } from '@angular/core';
import { environment } from 'src/environments/environment';

import { HttpClient } from '@angular/common/http';
import { Router } from '@angular/router';

import { ConditionalParser } from '../utils/conditional-parser';

import {
  ClientSideQuestion,
  QuestionAnswer,
  SaveQuestionAnswer,
} from '../models/question';
import { Questionnaire } from '../models/questionnaire';
import { Observable, map } from 'rxjs';

import { NotificationService } from './notification.service';

export { ClientSideQuestion, QuestionAnswer };

@Injectable()
export class QuestionsService {
  private parser: ConditionalParser;

  public questionnaireName = '';
  public questionnaireColor = '';
  private questionnaire: ClientSideQuestion[];
  questionnaireImage = '';

  public getCurrentCircleToFill(): number {
    switch (this.questionnaireName) {
      case 'Base':
        return 0;
      case 'Enfant':
        return 1;
      case 'Parent favorisé (PFA)':
        return 2;
      case 'Nouveau·elle conjoint·e (NC)':
        return 3;
    }

    return 0;
  }

  public showCannotSkipLastQuestionWarning = false;

  private currentSurveyID: string | null = null;

  constructor(
    private http: HttpClient,
    private notificationService: NotificationService,
    private router: Router
  ) {
    this.parser = new ConditionalParser();

    this.questionnaire = [];
  }

  public submitQuestionnaire() {
    const answers = this.questionnaire.reduce<
      { question_id: string; value: string }[]
    >((acc, question) => {
      if (question.answer === null) return acc;
      if (question.isConfirmed === false) return acc;

      const questionAnswer = {
        question_id: question.question_id,
        value: question.answer.toString(),
      } as SaveQuestionAnswer;

      if (question.otherValue) {
        questionAnswer.custom_answer = question.otherValue;
      }

      return [...acc, questionAnswer];
    }, []);

    // handle confirm or error

    this.http
      .post(
        environment.apiUrl + '/users_surveys/',
        { is_complete: true, survey_id: this.currentSurveyID },
        { observe: 'response' }
      )
      .subscribe((res) => {
        this.notificationService.show({
          message: 'Section terminée',
          type: 'success',
        });
        this.router.navigateByUrl('/dashboard');
      });

    return;
  }

  public getAllQuestionnaires(): Observable<Questionnaire[]> {
    return this.http.get<Questionnaire[]>(environment.apiUrl + '/survey');
  }

  public async getSingleQuestionnaire(questionnaireID: string) {
    this.http
      .get<Questionnaire>(`${environment.apiUrl}/surveys/${questionnaireID}`)
      .pipe(
        map((questionnaire) => {
          const questions = [
            ...questionnaire.questions,
          ] as ClientSideQuestion[];

          questions.forEach((question) => {
            question.shouldBeDisplayed = !question.condition;
            question.answer = question.answer || null;
            question.hasOtherValueToSpecify = false;
            question.otherValue = '';
            question.isConfirmed = question.answer !== null || false;

            question.isInfoBubbleOpen = false;

            switch (question.type) {
              case 'numeric-ladder':
                question.choices = [
                  { label: '0', value: '0' },
                  { label: '1', value: '1' },
                  { label: '2', value: '2' },
                  { label: '3', value: '3' },
                  { label: '4', value: '4' },
                  { label: '5', value: '5' },
                  { label: '6', value: '6' },
                  { label: '7', value: '7' },
                  { label: '8', value: '8' },
                  { label: '9', value: '9' },
                  { label: '10', value: '10' },
                ];
                break;
              case 'binary':
                question.choices = [
                  { label: 'Oui', value: '1' },

                  { label: 'Non', value: '0' },
                ];
                break;
            }
          });

          return questionnaire;
        })
      )
      .subscribe({
        next: (questionnaire) => {
          this.questionnaire = questionnaire.questions as ClientSideQuestion[];
          this.questionnaireName = questionnaire.name;
          this.questionnaireColor = questionnaire.color;
          this.questionnaireImage = questionnaire.cover_picture_url;
          this.currentSurveyID = questionnaire.survey_id;

          const root = document.querySelector(':root') as HTMLStyleElement;

          root.style.setProperty('--questionnaire-color', questionnaire.color);
        },
        error: (error) => {
          if (error.status === 401) {
            window.sessionStorage.clear();
            this.router.navigateByUrl('/auth-wall');
            return;
          }
          console.log(error);
          this.notificationService.show({
            message: 'Une erreur est survenue',
            type: 'danger',
          });
        },
      });
  }

  private getUnfilteredQuestions(): ClientSideQuestion[] {
    return this.questionnaire;
  }

  private checkIfSingleQuestionShouldBeDisplayed(
    question: ClientSideQuestion,
    questions: ClientSideQuestion[]
  ): void {
    if (!question.condition) return;

    const conditions = this.parser.parseCondition(question.condition);

    for (const {
      questionID,
      operator,
      conditionAnswer,
      logicalOperator,
    } of conditions) {
      const conditionQuestion = questions.find(
        (question) => question.question_id === questionID
      );
      if (!conditionQuestion) continue;

      let conditionMet = false;
      switch (operator) {
        case '>':
          conditionMet =
            conditionQuestion.answer !== null &&
            +conditionQuestion.answer > +conditionAnswer;
          break;
        case '<':
          conditionMet =
            conditionQuestion.answer !== null &&
            +conditionQuestion.answer < +conditionAnswer;
          break;

        case '=':
          conditionMet =
            conditionQuestion.answer !== null &&
            (/,/.test(conditionQuestion.answer)
              ? conditionQuestion.answer
                  .split(',')
                  .includes(conditionAnswer.toString())
              : +conditionQuestion.answer === +conditionAnswer);
          break;
        case '>=':
          conditionMet =
            conditionQuestion.answer !== null &&
            +conditionQuestion.answer >= +conditionAnswer;
          break;
        case '<=':
          conditionMet =
            conditionQuestion.answer !== null &&
            +conditionQuestion.answer <= +conditionAnswer;
          break;
        default:
          throw new Error('Unknown operator');
      }

      if (logicalOperator === undefined && conditionMet) {
        question.shouldBeDisplayed = true;
        return;
      }

      if (logicalOperator === '||' && conditionMet) {
        question.shouldBeDisplayed = true;
        return;
      } else if (logicalOperator === '&&' && !conditionMet) {
        question.shouldBeDisplayed = false;
        question.answer = null;
        return;
      }
    }

    // If none of the conditions returned early, all "&&" conditions were met or no conditions with "||" were met
    question.shouldBeDisplayed =
      conditions[conditions.length - 1].logicalOperator === '&&';
  }

  // TODO (simon) -> old method
  // private checkIfSingleQuestionShouldBeDisplayed(
  //   question: ClientSideQuestion,
  //   questions: ClientSideQuestion[]
  // ): void {
  //   if (!question.condition) return;

  //   const [questionID, operator, conditionAnswer] = this.parser.parseCondition(
  //     question.condition
  //   );

  //   const conditionQuestion = questions.find(
  //     (question) => question.question_id === questionID
  //   );
  //   if (!conditionQuestion) return;

  //   switch (operator) {
  //     case '>':
  //       if (
  //         conditionQuestion.answer !== null &&
  //         +conditionQuestion.answer > +conditionAnswer
  //       ) {
  //         question.shouldBeDisplayed = true;
  //       } else {
  //         question.shouldBeDisplayed = false;
  //         question.answer = null;
  //       }
  //       //
  //       break;
  //     case '<':
  //       if (
  //         conditionQuestion.answer !== null &&
  //         +conditionQuestion.answer < +conditionAnswer
  //       ) {
  //         question.shouldBeDisplayed = true;
  //       } else {
  //         question.shouldBeDisplayed = false;
  //         question.answer = null;
  //       }
  //       break;

  //     case '=':
  //       if (
  //         conditionQuestion.answer !== null &&
  //         (/,/.test(conditionQuestion.answer)
  //           ? conditionQuestion.answer
  //               .split(',')
  //               .includes(conditionAnswer.toString())
  //           : +conditionQuestion.answer === +conditionAnswer)
  //       ) {
  //         question.shouldBeDisplayed = true;
  //       } else {
  //         question.shouldBeDisplayed = false;
  //         question.answer = null;
  //       }
  //       break;

  //     case '>=':
  //       if (
  //         conditionQuestion.answer !== null &&
  //         +conditionQuestion.answer >= +conditionAnswer
  //       ) {
  //         question.shouldBeDisplayed = true;
  //       } else {
  //         question.shouldBeDisplayed = false;
  //         question.answer = null;
  //       }
  //       break;

  //     case '<=':
  //       if (
  //         conditionQuestion.answer !== null &&
  //         +conditionQuestion.answer <= +conditionAnswer
  //       ) {
  //         question.shouldBeDisplayed = true;
  //       } else {
  //         question.shouldBeDisplayed = false;
  //         question.answer = null;
  //       }
  //       break;

  //     default:
  //       throw new Error('Unknown operator');
  //   }
  // }

  // todo cleanup this one
  private checkIfQuestionsShouldBeDisplayed(): void {
    const questions = this.questionnaire;
    // add all questions answered by user from backend

    questions.forEach((question) =>
      this.checkIfSingleQuestionShouldBeDisplayed(question, questions)
    );
  }

  getQuestions(): ClientSideQuestion[] {
    const questions = this.getUnfilteredQuestions();

    return questions.filter((question) => question.shouldBeDisplayed);
  }

  private getProgressPercentage(): number {
    const questions = this.getQuestions();

    const answeredQuestions = questions.filter(
      (question) => question.answer !== null
    );

    const hiddenQuestions = questions.filter(
      (question) => !question.shouldBeDisplayed
    );

    return (
      (answeredQuestions.length / (questions.length - hiddenQuestions.length)) *
      100
    );
  }

  public getProgress(): string {
    const progress = this.getProgressPercentage();

    const roundedProgress = Math.round(progress) + '%';

    return roundedProgress;
  }

  public isDone(): boolean {
    return this.getProgressPercentage() === 100;
  }

  public onSave() {
    // todo validate
    this.submitQuestionnaire();
  }

  public reset() {
    const questions = this.getUnfilteredQuestions();

    questions.forEach((question) => {
      question.answer = null;
      question.isConfirmed = false;
    });

    this.checkIfQuestionsShouldBeDisplayed();
  }

  public getIsCompleted(): boolean {
    let allCompleted = true;

    const questions = this.getQuestions();

    for (let i = 0; i < questions.length; i++) {
      if (questions[i].answer) continue;

      allCompleted = false;
      break;
    }

    return allCompleted;
  }

  private handleMultipleChoicesSelect(
    question: ClientSideQuestion,
    answer: QuestionAnswer
  ): QuestionAnswer {
    if (answer === null) return answer;

    if (question.type !== 'select-multiple') return answer;

    if (question.answer === null) return answer;

    const answers = question.answer.split(',');

    if (answers.includes(answer)) {
      answers.splice(answers.indexOf(answer), 1);
    } else {
      answers.push(answer);
    }

    return answers.join(',') || null;
  }

  private handleAutomaticallyMarkAsConfirmed(
    question: ClientSideQuestion
  ): void {
    if (question.answer === 'custom') return;

    if (
      question.type === 'select-single' ||
      question.type === 'numeric-ladder' ||
      question.type === 'labeled-ladder' ||
      question.type === 'binary'
    ) {
      question.isConfirmed = true;
    }
  }

  public onAnswer(question: ClientSideQuestion, answer: QuestionAnswer): void {
    question.isConfirmed = false;
    question.answer = this.handleMultipleChoicesSelect(question, answer);

    question.hasOtherValueToSpecify = false;

    if (answer !== null && question.choices && answer === 'custom') {
      question.hasOtherValueToSpecify = true;
    }

    question.isInfoBubbleOpen = false;

    this.handleAutomaticallyMarkAsConfirmed(question);

    this.checkIfQuestionsShouldBeDisplayed();

    this.http
      .post<{ message: string }>(
        environment.apiUrl + '/answers',
        {
          answers: [
            {
              question_id: question.question_id,
              value: answer,
            },
          ],
        },
        { observe: 'response' }
      )
      .subscribe({
        next: (response) => {
          console.log({ response });
        },
        error: (error) => {
          console.log({ error });
        },
      });
  }

  public onSkip(question: ClientSideQuestion): void {
    const questionIndex = this.questionnaire.indexOf(question);

    if (questionIndex === this.questionnaire.length - 1) {
      this.showCannotSkipLastQuestionWarning = true;

      setTimeout(() => {
        this.showCannotSkipLastQuestionWarning = false;
      }, 2000);
    }

    this.questionnaire.splice(questionIndex, 1);

    this.questionnaire.push(question);

    this.checkIfQuestionsShouldBeDisplayed();
  }

  onInfoBubbleToggle(question: ClientSideQuestion): void {
    question.isInfoBubbleOpen = !question.isInfoBubbleOpen;
  }

  private validateCannotConfirm(question: ClientSideQuestion): boolean {
    if (question.type === 'integer') {
      if (question.answer === null) return true;

      if (question.min_value === undefined) return false;
      if (question.max_value === undefined) return false;

      if (
        +question.answer < question.min_value ||
        +question.answer > question.max_value
      ) {
        return true;
      }
    }

    return false;
  }

  public onToggleConfirm(question: ClientSideQuestion): void {
    if (this.validateCannotConfirm(question)) return;

    question.isConfirmed = !question.isConfirmed;
  }
}