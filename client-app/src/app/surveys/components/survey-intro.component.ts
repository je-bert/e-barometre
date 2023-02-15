import { Component } from '@angular/core';

@Component({
  selector: 'app-survey-intro',
  template: `
    <section class="container-fluid bg-overlay-content bg-light -tw-mt-20">
      <div class="row">
        <div class="col-lg-4 col-sm-6 mb-grid-gutter">
          <div class="card h-100 border-0 shadow-lg py-4">
            <div class="card-body text-center">
              <i
                class="ai-map-pin mb-4 tw-text-4xl tw-text-[var(--questionnaire-color)]"
              ></i>
              <h3 class="h6 mb-2">Objectif</h3>
              <p class="fs-sm mb-2">lorem lorem lorem</p>
            </div>
          </div>
        </div>
        <div class="col-lg-4 col-sm-6 mb-grid-gutter">
          <div class="card h-100 border-0 shadow-lg py-4">
            <div class="card-body text-center">
              <i
                class="ai-clock mb-4 tw-text-4xl tw-text-[var(--questionnaire-color)]"
              ></i>
              <h3 class="h6 mb-2">Temps requis</h3>
              <ul class="list-unstyled fs-sm mb-0">
                <li>Entre 1h et 1h30</li>
              </ul>
            </div>
          </div>
        </div>
        <div class="col-lg-4 col-sm-6 mb-grid-gutter">
          <div class="card h-100 border-0 shadow-lg py-4">
            <div class="card-body text-center">
              <i
                class="ai-info mb-4 tw-text-4xl tw-text-[var(--questionnaire-color)]"
              ></i>
              <h3 class="h6 mb-2">Lorem</h3>
              <ul class="list-unstyled fs-sm mb-0">
                <li>Trucs? À se souvenir, etc.</li>
              </ul>
            </div>
          </div>
        </div>
      </div>
    </section>
  `,
  styles: [],
})
export class SurveyIntroComponent {}
