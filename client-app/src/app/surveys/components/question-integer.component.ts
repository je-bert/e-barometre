import { Component, Input } from '@angular/core';

@Component({
  selector: 'app-question-integer',
  template: `
 <div class="my-4 tw-flex tw-justify-center tw-relative">
  <div class="custom-number-input">
    <div class="count-input ms-n3 tw-flex">
      <button
        class="btn btn-icon tw-text-lg"
        type="button"
 
      >
        -
      </button>
      <input
        type="number"
        [max]="question.max_value || 100"
        [min]="question.min_value || 0"

        class="form-control tw-w-32"
      />
      <button
        class="btn btn-icon tw-text-lg"
        type="button"

      >
        +
      </button>
    </div>

    <div class="invalid-feedback tw-absolute tw-bottom-[-50%]">
      Veuillez entrer un chiffre entre {{ question.min_value }} et
      {{ question.max_value }}
    </div>
  </div>
</div>

  `,
  styles: [
  ]
})
export class QuestionIntegerComponent {
  @Input() question!: any

}
