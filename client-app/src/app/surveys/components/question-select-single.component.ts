import { Component, EventEmitter, Input, Output } from '@angular/core';

@Component({
  selector: 'app-question-select-single',
  template: `
  <div class="tw-w-full tw-flex tw-justify-center tw-flex-wrap">
  <button
    (click)="handleClick(answer.value)"
    *ngFor="let answer of question.choices"
    type="button"
    [ngClass]="{
      'btn-outline-primary': answer.value !== question.answer,
      'btn-success':
        answer.value === question.answer ||
        (question.answer &&
          answer.value &&
          question.answer.indexOf(answer.value) > -1)
    }"
    class="btn btn-icon tw-mx-4 tw-mb-4 tw-whitespace-pre-wrap tw-break-words"
  >
    <p class="tw-mb-0">
      {{ answer.label }}
    </p>
  </button>
</div>

  `,
  styles: [
  ]
})
export class QuestionSelectSingleComponent {

  @Input() question!: any;

  @Output() questionAnswered = new EventEmitter<{ questionId: string; questionAnswer: string }>()

  handleClick(answer: string) {
    this.questionAnswered.emit({ questionId: this.question.question_id, questionAnswer: answer })
  }

}
