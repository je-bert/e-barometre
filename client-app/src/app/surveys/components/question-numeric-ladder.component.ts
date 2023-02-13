import { Component, Input } from '@angular/core';

@Component({
  selector: 'app-question-numeric-ladder',
  template: `
<div class="tw-flex">
  <div class="tw-w-1/6">
    <p class="tw-text-center tw-font-bold tw-text-questionnaire tw-uppercase">
      Aucune
    </p>
  </div>
  <div class="tw-w-2/3 tw-flex tw-justify-center">
    <button
      *ngFor="let answer of question.choices"
      type="button"
      [ngClass]="{
        'btn-outline-primary': answer.value !== question.answer,
        'btn-success': answer.value === question.answer
      }"
      class="btn btn-icon tw-mx-1 tw-w-14"
    >
      <p *ngIf="answer.value !== question.answer" class="tw-mb-0">
        {{ answer.label }}
      </p>
      <i *ngIf="answer.value === question.answer" class="ai-check"></i>
    </button>
  </div>
  <div class="tw-w-1/6">
    <p class="tw-text-center tw-font-bold tw-text-questionnaire tw-uppercase">
      Excellente
    </p>
  </div>
</div>
  `,
  styles: [
  ]
})
export class QuestionNumericLadderComponent {
  @Input() question!: any

}
