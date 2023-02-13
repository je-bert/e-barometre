import { Component, Input } from '@angular/core';

@Component({
  selector: 'app-question-select-multiple',
  template: `
<div class="tw-w-full tw-flex tw-justify-center tw-flex-wrap">
  <button
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
export class QuestionSelectMultipleComponent {
  @Input() question!: any

}