import {
  Component,
  EventEmitter,
  Input,
  Output,
  ElementRef,
} from '@angular/core';
import { timer } from 'rxjs';

@Component({
  selector: 'app-question',
  template: `
  <app-question-info-bubble
  *ngIf="question.info_bubble_text"
  [text]="question.info_bubble_text"

 />

 {{question.question_id | json}}
 {{question.condition | json}}


<div [ngSwitch]="question.type" class="card shadow-lg tw-relative">
  <div class="card-body tw-p-12">
    <h5 class="card-title tw-text-center tw-mb-10 tw-font-semibold">
      {{ question.intro }}
      <br *ngIf="question.intro" />
      {{ question.title }}

      <ng-container *ngIf="question.type === 'select-multiple'">
        <br />
        <i class="tw-inline-block tw-mt-2">
          (choisir un ou plusieurs parmis les suivants)
        </i>
      </ng-container>
    </h5>

    <!-- Question types -->

    <ng-container *ngSwitchCase="'labeled-ladder'">
      <app-question-labeled-ladder
 
        [question]="question"
        (questionAnswered)="questionAnswered.emit($event)"
      />
    </ng-container>

    <ng-container *ngSwitchCase="'numeric-ladder'">
      <app-question-numeric-ladder

        [question]="question"
      />
    </ng-container>

    <ng-container *ngSwitchCase="'integer'">
      <app-question-integer
      (questionAnswered)="questionAnswered.emit($event)"
        [answer]="answer"
    
        [question]="question" />
    </ng-container>

    <ng-container *ngSwitchCase="'select-single'">
    
      <app-question-select-single
      (questionAnswered)="questionAnswered.emit($event)"
      [answer]="answer"
    
        [question]="question" />
    </ng-container>

    <ng-container *ngSwitchCase="'select-multiple'">
      <app-question-select-multiple

      (questionAnswered)="questionAnswered.emit($event)"
        [answer]="answer"
        [question]="question"
      />
    </ng-container>

    <ng-container *ngSwitchCase="'binary'">
      <app-question-select-single
       (questionAnswered)="questionAnswered.emit($event)"
        [answer]="answer"
        [question]="question" />
    </ng-container>

    <!-- End Question types -->

    <ng-container *ngIf="question.hasOtherValueToSpecify">
      <div class="my-4 row align-items-center">
        <label class="col-md-2 col-form-label tw-text-end" for="text-input"
          >Spécifiez:</label
        >
        <div class="col-md-10">
          <input
            type="text"
            class="form-control"

            name="Other value for {{ question.title }}"
          />
        </div>
      </div>
    </ng-container>
  </div>

 
</div>

  `,
  styles: [``],
})
export class QuestionComponent {
  @Input() question!: any;
  @Input() answer!: string | null;

  @Output() questionAnswered = new EventEmitter<{
    questionId: string;
    questionAnswer: string;
  }>();

  self: HTMLElement | null = null;

  onQuestionAnswered(event: any) {
    this.questionAnswered.emit(event);
  }

  constructor(private elRef: ElementRef) {
    this.self = elRef.nativeElement as HTMLElement;

    this.self.addEventListener('click', (event) => {
      timer(150).subscribe(() => {
        this.self?.parentElement?.nextElementSibling?.firstElementChild?.scrollIntoView(
          {
            behavior: 'smooth',
            block: 'center',
          }
        );
      });
    });
  }
}
