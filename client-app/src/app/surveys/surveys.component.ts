import { Component } from '@angular/core';

@Component({
  selector: 'app-surveys',
  template: `
    <app-navbar/>
    <app-header [isSurvey]="true"/>
    <main class="page-wrapper tw-min-h-[94vh]">
      <router-outlet/>
    </main>
   <app-footer/>
  `,
  styles: [],
})
export class SurveysComponent {}
