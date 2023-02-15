import { Component, EventEmitter, Input, Output } from '@angular/core';

@Component({
  selector: 'app-question-labeled-ladder',
  template: `
    <div class="tw-flex tw-justify-center tw-relative">
      <mat-radio-group>
        <ng-container *ngFor="let answer of question.choices">
          <mat-radio-button
            [ngClass]="{
              'app-answer-so tw-absolute -tw-bottom-10 -tw-right-4':
                answer.label === 'Sans objet'
            }"
            (click)="handleClick(answer.value)"
            [value]="answer"
            >{{ answer.label }}</mat-radio-button
          >
        </ng-container>
      </mat-radio-group>
    </div>
  `,
  styles: [],
})
export class QuestionLabeledLadderComponent {
  @Input() question!: any;

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
