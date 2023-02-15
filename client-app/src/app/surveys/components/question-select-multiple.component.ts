import { Component, Input, Output, EventEmitter } from '@angular/core';

@Component({
  selector: 'app-question-select-multiple',
  template: `
    <div class="tw-w-full tw-flex tw-justify-center tw-flex-wrap">
      <button
        *ngFor="let choice of question.choices"
        (click)="$event.stopPropagation(); onClick(choice.value)"
        type="button"
        [ngClass]="{
          'btn-outline-primary': selectedAnswer.indexOf(choice.value) === -1,
          'btn-success': selectedAnswer.indexOf(choice.value) > -1
        }"
        class="btn btn-icon tw-mx-4 tw-mb-4 tw-whitespace-pre-wrap tw-break-words"
      >
        <p class="tw-mb-0">
          {{ choice.label }}
        </p>
      </button>
    </div>
    <div class="tw-flex tw-justify-center tw-mb-8 tw-mt-8">
      <button
        (click)="onConfirmAnswers()"
        class="btn btn-primary"
        [disabled]="selectedAnswer.length === 0"
      >
        <span *ngIf="question.isConfirmed">Réponse confirmé</span>
        <span *ngIf="!question.isConfirmed">Confirmer les choix</span>
      </button>
    </div>
  `,
  styles: [],
})
export class QuestionSelectMultipleComponent {
  @Input() question!: any;
  @Input() answer!: string | null;

  selectedAnswer: string[] = [];

  onClick(answer: string) {
    if (this.selectedAnswer.includes(answer)) {
      this.selectedAnswer = this.selectedAnswer.filter(
        (selectedAnswer) => selectedAnswer !== answer
      );
      return;
    }

    this.selectedAnswer.push(answer);
  }

  @Output() questionAnswered = new EventEmitter<{
    questionId: string;
    questionAnswer: string;
  }>();

  ngOnInit() {
    if (this.answer) {
      this.selectedAnswer = this.answer.split(',');
    }
  }

  onConfirmAnswers() {
    this.questionAnswered.emit({
      questionId: this.question.question_id,
      questionAnswer: this.selectedAnswer.join(','),
    });
  }
}
