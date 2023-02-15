import { Component, Input } from '@angular/core';

@Component({
  selector: 'app-header',
  template: `
    <section
      class="position-relative pt-7 pb-5 pb-md-7 bg-size-cover bg-attachment-fixed"
      [ngClass]="{
        'tw-bg-[url(/assets/img/blue_gradient_bg.png)]': !isSurvey,
        'tw-bg-[var(--questionnaire-color)]': isSurvey
      }"
    >
      <div class="shape shape-bottom shape-curve bg-body bg-light">
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 3000 185.4">
          <path
            fill="currentColor"
            d="M3000,0v185.4H0V0c496.4,115.6,996.4,173.4,1500,173.4S2503.6,115.6,3000,0z"
          ></path>
        </svg>
      </div>
      <div
        class="
      container
      position-relative
      zindex-5
      text-center
      pt-md-6 pt-lg-7
      py-5
      my-lg-3
    "
      >
        <h1 class="text-light mb-0 display-3">Questionnaire Base</h1>
      </div>
    </section>
  `,
  styles: [],
})
export class HeaderComponent {
  @Input() isSurvey = false;
}
