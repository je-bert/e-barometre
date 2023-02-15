import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';

import { SurveysRoutingModule } from './surveys-routing.module';
import { SurveysComponent } from './surveys.component';
import { SharedModule } from '../shared/shared.module';
import { SurveyListComponent } from './containers/survey-list.component';
import { QuestionListComponent } from './containers/question-list.component';
import { SurveyIntroComponent } from './components/survey-intro.component';
import { ProgressBarComponent } from './components/progress-bar.component';
import { SingleSurveyComponent } from './containers/single-survey.component';
import { SurveyFooterComponent } from './components/survey-footer.component';
import { QuestionComponent } from './components/question.component';
import { QuestionInfoBubbleComponent } from './components/question-info-bubble.component';
import { QuestionLabeledLadderComponent } from './components/question-labeled-ladder.component';
import { QuestionIntegerComponent } from './components/question-integer.component';
import { QuestionNumericLadderComponent } from './components/question-numeric-ladder.component';
import { QuestionSelectMultipleComponent } from './components/question-select-multiple.component';
import { QuestionSelectSingleComponent } from './components/question-select-single.component';

import { MatRadioModule } from '@angular/material/radio';
import { MatIconModule } from '@angular/material/icon';
import { MatButtonModule } from '@angular/material/button';

@NgModule({
  declarations: [
    SurveysComponent,
    SurveyListComponent,
    QuestionListComponent,
    SurveyIntroComponent,
    ProgressBarComponent,
    SingleSurveyComponent,
    SurveyFooterComponent,
    QuestionComponent,
    QuestionInfoBubbleComponent,
    QuestionLabeledLadderComponent,
    QuestionIntegerComponent,
    QuestionNumericLadderComponent,
    QuestionSelectMultipleComponent,
    QuestionSelectSingleComponent,
  ],
  imports: [
    CommonModule,
    SurveysRoutingModule,
    SharedModule,
    MatRadioModule,
    MatIconModule,
    MatButtonModule,
  ],
})
export class SurveysModule {}
