import { Component, Input, ChangeDetectionStrategy } from '@angular/core';

@Component({
  changeDetection: ChangeDetectionStrategy.OnPush,
  selector: 'app-progress-bar',
  template: `
    <div
      class="
    tw-sticky
    tw-top-36
    tw-w-1/2
    tw-pt-12
    tw-pb-60
    tw-rounded-3xl
    tw-mt-36
    tw-shadow-lg
  "
      style="background-color: var(--questionnaire-color)"
    >
      <div class="tw-mb-4">
        <h3
          class="tw-text-center tw-text-white h6"
          style="font-family: 'Poppins'"
        >
          {{ progress }}
        </h3>
      </div>

      <div
        style="background-color: #f3f3f9"
        class="tw-h-96 tw-w-4 tw-rounded-xl tw-mx-auto"
      >
        <div
          [style.height]="progress"
          [style.backgroundColor]="'#030d45'"
          class="
        tw-w-full
        tw-rounded-t-xl
        tw-transition-all
        tw-duration-500
        tw-ease-linear
      "
          [ngClass]="{ 'tw-rounded-xl': progress === '100%' }"
        ></div>
      </div>
      <div class="tw-absolute tw-bottom-12 tw-w-full">
        <h3
          class="h6 tw-text-white"
          style="transform: rotate(270deg); white-space: nowrap"
        >
          Questionnaire demo
        </h3>
      </div>
    </div>
  `,
  styles: [],
})
export class ProgressBarComponent {
  @Input() progress!: string;
}
