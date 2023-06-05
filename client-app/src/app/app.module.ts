import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { HttpClientModule } from '@angular/common/http';
import { httpInterceptorProviders } from './http-interceptors';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { NavbarComponent } from './components/shared/navbar/navbar.component';
import { PageHeaderComponent } from './components/shared/page-header/page-header.component';
import { FooterComponent } from './components/shared/footer/footer.component';
import { ContactFormComponent } from './components/shared/contact-form/contact-form.component';
import { HelpComponent } from './components/auth/help/help.component';
import { AdminComponent } from './components/admin/admin.component';
import { ForgotPasswordComponent } from './components/auth-wall/forgot-password/forgot-password.component';
import { LoginComponent } from './components/auth-wall/login/login.component';
import { SignupComponent } from './components/auth-wall/signup/signup.component';
import { TermsAndConditionsComponent } from './components/auth/terms-and-conditions/terms-and-conditions.component';
import { AccountComponent } from './components/auth/account/account.component';
import { LegalComponent } from './components/auth/legal/legal.component';
import { AuthWallComponent } from './components/auth-wall/auth-wall.component';
import { AuthComponent } from './components/auth/auth.component';
import { ResourcesComponent } from './components/auth/resources/resources.component';
import { ReportsComponent } from './components/auth/reports/reports.component';
import { MyAccountComponent } from './components/auth/my-account/my-account.component';
import { ProfileComponent } from './components/auth/my-account/profile/profile.component';
import { OrdersComponent } from './components/auth/my-account/orders/orders.component';
import { ResourceComponent } from './components/auth/resource/resource.component';
import { QuestionnairesComponent } from './components/auth/questionnaires/questionnaires.component';
import { QuestionnaireComponent } from './components/auth/questionnaire/questionnaire.component';
import { InfoBubbleComponent } from './components/auth/questionnaire/info-bubble/info-bubble.component';
import { ProgressBarComponent } from './components/auth/questionnaire/progress-bar/progress-bar.component';
import { QuestionDetailsComponent } from './components/auth/questionnaire/question-details/question-details.component';
import { QuestionsContainerComponent } from './components/auth/questionnaire/questions-container/questions-container.component';
import { QuestionsListComponent } from './components/auth/questionnaire/questions-list/questions-list.component';
import { DashboardComponent } from './components/auth/dashboard/dashboard.component';
import { CannotSkipLastWarningComponent } from './components/auth/questionnaire/cannot-skip-last-warning/cannot-skip-last-warning.component';
import { NotificationComponent } from './components/shared/notification/notification.component';
import { TestsComponent } from './components/auth/tests/tests.component';
import { NumericLadderComponent } from './components/auth/questionnaire/question-details/numeric-ladder/numeric-ladder.component';
import { LabeledLadderComponent } from './components/auth/questionnaire/question-details/labeled-ladder/labeled-ladder.component';
import { IntegerComponent } from './components/auth/questionnaire/question-details/integer/integer.component';
import { SelectSingleComponent } from './components/auth/questionnaire/question-details/select-single/select-single.component';
import { SelectMultipleComponent } from './components/auth/questionnaire/question-details/select-multiple/select-multiple.component';
import { AdminPanelComponent } from './components/admin/admin-panel/admin-panel.component';
import { AdminLoginComponent } from './components/admin/admin-login/admin-login.component';
import { AdminSurveysTableComponent } from './components/admin/admin-surveys-table/admin-surveys-table.component';

// material

import { MatButtonModule } from '@angular/material/button';
import { MatIconModule } from '@angular/material/icon';
import { MatMenuModule } from '@angular/material/menu';
import { MatProgressSpinnerModule } from '@angular/material/progress-spinner';
import { MatSnackBarModule } from '@angular/material/snack-bar';
import { MatCardModule } from '@angular/material/card';
import { MatExpansionModule } from '@angular/material/expansion';
import { MatSidenavModule } from '@angular/material/sidenav';
import { MatToolbarModule } from '@angular/material/toolbar';
import { MatTooltipModule } from '@angular/material/tooltip';
import { MatFormFieldModule } from '@angular/material/form-field';
import { MatInputModule } from '@angular/material/input';
import { MatRadioModule } from '@angular/material/radio';

// clarity design

import { ClarityModule } from '@clr/angular';
import { AdminSurveyTableComponent } from './components/admin/admin-survey-table/admin-survey-table.component';
import { AdminAnswersComponent } from './components/admin/admin-answers/admin-answers.component';
import { AdminSurveyChoicesComponent } from './components/admin/admin-survey-choices/admin-survey-choices.component';
import { AdminSurveyAnswersComponent } from './components/admin/admin-survey-answers/admin-survey-answers.component';
import { MatDialogModule } from '@angular/material/dialog';
import { DialogComponent } from './components/shared/dialog/dialog.component';
import { AvailableQuestionnairesComponent } from './components/auth/my-account/available-questionnaires/available-questionnaires.component';
import { FinalReportsComponent } from './components/auth/my-account/final-reports/final-reports.component';
import { AdminGlossaryComponent } from './components/admin/admin-glossary/admin-glossary.component';
import { SvgParentRepondantComponent } from './components/auth/svg/svg-parent-repondant/svg-parent-repondant.component';
import { SvgEnfantComponent } from './components/auth/svg/svg-enfant/svg-enfant.component';
import { SvgCoparentComponent } from './components/auth/svg/svg-coparent/svg-coparent.component';
import { SvgNouveauConjointComponent } from './components/auth/svg/svg-nouveau-conjoint/svg-nouveau-conjoint.component';
import { PresentationDropdownComponent } from './components/auth/dashboard/presentation-dropdown.component';
import { SingleReportPresentationComponent } from './components/auth/reports/single-report-presentation.component';
import { SingleReportComponent } from './components/auth/reports/single-report.component';

@NgModule({
  declarations: [
    AppComponent,
    NavbarComponent,
    PageHeaderComponent,
    FooterComponent,
    ContactFormComponent,
    HelpComponent,
    AdminComponent,
    ForgotPasswordComponent,
    LoginComponent,
    SignupComponent,
    TermsAndConditionsComponent,
    AccountComponent,
    LegalComponent,
    AuthWallComponent,
    AuthComponent,
    ResourcesComponent,
    ReportsComponent,
    MyAccountComponent,
    ProfileComponent,
    OrdersComponent,
    ResourceComponent,
    QuestionnairesComponent,
    QuestionnaireComponent,
    InfoBubbleComponent,
    ProgressBarComponent,
    QuestionDetailsComponent,
    QuestionsContainerComponent,
    QuestionsListComponent,
    DashboardComponent,
    CannotSkipLastWarningComponent,
    NotificationComponent,
    TestsComponent,
    NumericLadderComponent,
    LabeledLadderComponent,
    IntegerComponent,

    SelectSingleComponent,
    SelectMultipleComponent,
    AdminPanelComponent,
    AdminLoginComponent,
    AdminSurveysTableComponent,
    AdminSurveyTableComponent,
    AdminAnswersComponent,
    AdminSurveyChoicesComponent,
    AdminSurveyAnswersComponent,
    DialogComponent,
    AvailableQuestionnairesComponent,
    FinalReportsComponent,
    AdminGlossaryComponent,
    SvgParentRepondantComponent,
    SvgEnfantComponent,
    SvgCoparentComponent,
    SvgNouveauConjointComponent,
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    FormsModule,
    ReactiveFormsModule,
    BrowserAnimationsModule,
    HttpClientModule,
    PresentationDropdownComponent,
    SingleReportPresentationComponent,
    SingleReportComponent,

    // material
    MatButtonModule,
    MatIconModule,
    MatMenuModule,
    MatProgressSpinnerModule,
    MatSnackBarModule,
    MatExpansionModule,
    MatCardModule,
    MatSidenavModule,
    MatToolbarModule,
    MatTooltipModule,
    MatDialogModule,
    MatFormFieldModule,
    MatInputModule,
    MatRadioModule,

    // clarity design
    ClarityModule,
  ],
  providers: [httpInterceptorProviders],
  exports: [PageHeaderComponent],
  bootstrap: [AppComponent],
})
export class AppModule {}
