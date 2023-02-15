import { Component, Input, ChangeDetectionStrategy } from '@angular/core';
import { Subject } from 'rxjs';
import { startWith, scan } from 'rxjs/operators';

@Component({
  changeDetection: ChangeDetectionStrategy.OnPush,
  selector: 'app-question-info-bubble',
  template: `
    <div
      class="tw-absolute tw-right-0 tw-top-2 tw-z-10 tw-cursor-pointer tw-w-80"
    >
      <button
        (click)="handleToggle()"
        mat-mini-fab
        color="primary"
        class="me-3 tw-absolute tw-right-0"
      >
        <svg
          height="16"
          width="16"
          xmlns="http://www.w3.org/2000/svg"
          viewBox="0 0 192 512"
        >
          <!--! Font Awesome Pro 6.2.0 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license (Commercial License) Copyright 2022 Fonticons, Inc. -->
          <path
            fill="white"
            d="M144 80c0 26.5-21.5 48-48 48s-48-21.5-48-48s21.5-48 48-48s48 21.5 48 48zM0 224c0-17.7 14.3-32 32-32H96c17.7 0 32 14.3 32 32V448h32c17.7 0 32 14.3 32 32s-14.3 32-32 32H32c-17.7 0-32-14.3-32-32s14.3-32 32-32H64V256H32c-17.7 0-32-14.3-32-32z"
          />
        </svg>
      </button>

      <div
        *ngIf="isToggled$ | async"
        class="popover bs-popover-start bs-popover-start-demo mt-2 tw-relative"
        role="tooltip"
      >
        <div class="popover-arrow"></div>
        <h3 class="popover-header">Information</h3>
        <div class="popover-body tw-h-44 tw-overflow-y-scroll">
          {{ text }}
        </div>
      </div>
    </div>
  `,
  styles: [],
})
export class QuestionInfoBubbleComponent {
  @Input() text!: string;

  private toggler$ = new Subject<void>();

  isToggled$ = this.toggler$.asObservable().pipe(
    startWith(false),
    scan((acc) => !acc)
  );

  handleToggle() {
    this.toggler$.next();
  }
}
