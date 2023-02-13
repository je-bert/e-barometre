import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { SingleSurveyComponent } from './containers/single-survey.component';
import { SurveysComponent } from './surveys.component';

const routes: Routes = [{
  path: '', component: SurveysComponent, children: [
    { path: 'demo', component: SingleSurveyComponent },
    { path: '**', redirectTo: 'demo' }
  ]
}];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class SurveysRoutingModule { }
