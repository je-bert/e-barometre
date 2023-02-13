import { Component, EventEmitter, Input, Output } from '@angular/core';

@Component({
  selector: 'app-question',
  template: `
  <app-question-info-bubble

  [question]="question"/>


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
    
        [question]="question" />
    </ng-container>

    <ng-container *ngSwitchCase="'select-single'">
      <app-question-select-single
      (questionAnswered)="questionAnswered.emit($event)"
    
        [question]="question" />
    </ng-container>

    <ng-container *ngSwitchCase="'select-multiple'">
      <app-question-select-multiple

        [question]="question"
      />
    </ng-container>

    <ng-container *ngSwitchCase="'binary'">
      <app-question-select-single

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

  <div
    *ngIf="question.type === 'select-multiple'"
    class="tw-flex tw-justify-center tw-mb-12"
  >
    <button
      class="btn btn-primary"
      [disabled]="question.answer === null"
    >
      <span *ngIf="question.isConfirmed">Réponse confirmé</span>
      <span *ngIf="!question.isConfirmed">Confirmer les choix</span>
    </button>
  </div>
</div>

  `,
  styles: [
  ]
})
export class QuestionComponent {

  @Input() question!: any



  @Output() questionAnswered = new EventEmitter<{ questionId: string; questionAnswer: string }>();


}
