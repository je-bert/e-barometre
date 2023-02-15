import {
  Component,
  EventEmitter,
  Input,
  Output,
  ChangeDetectionStrategy,
  SimpleChanges,
} from '@angular/core';

@Component({
  changeDetection: ChangeDetectionStrategy.OnPush,
  selector: 'app-question-select-single',
  template: `
    <div class="tw-w-full tw-flex tw-justify-center tw-flex-wrap">
      <button
        (click)="handleClick(choice.value)"
        *ngFor="let choice of question.choices"
        type="button"
        [ngClass]="{
          'btn-outline-primary': choice.value !== answer,
          'btn-success':
            choice.value === answer ||
            (answer && choice.value && answer.indexOf(choice.value) > -1)
        }"
        class="btn btn-icon tw-mx-4 tw-mb-4 tw-whitespace-pre-wrap tw-break-words"
      >
        <p class="tw-mb-0">
          {{ choice.label }}
        </p>
      </button>
    </div>
  `,
  styles: [],
})
export class QuestionSelectSingleComponent {
  @Input() question!: any;
  @Input() answer!: string | null;

  @Output() questionAnswered = new EventEmitter<{
    questionId: string;
    questionAnswer: string;
  }>();

  handleClick(answer: string) {
    this.questionAnswered.emit({
      questionId: this.question.question_id,
      questionAnswer: answer,
    });
  }
}
