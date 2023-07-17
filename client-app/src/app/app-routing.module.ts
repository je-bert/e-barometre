import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';

import { AuthGuard } from './guards/auth.guard';

import { LoginComponent } from './components/auth-wall/login/login.component';
import { SignupComponent } from './components/auth-wall/signup/signup.component';
import { ForgotPasswordComponent } from './components/auth-wall/forgot-password/forgot-password.component';
import { AuthWallComponent } from './components/auth-wall/auth-wall.component';
import { AuthComponent } from './components/auth/auth.component';
import { AdminPanelComponent } from './components/admin/admin-panel/admin-panel.component';

import { ReportsComponent } from './components/auth/reports/reports.component';
import { MyAccountComponent } from './components/auth/my-account/my-account.component';
import { ProfileComponent } from './components/auth/my-account/profile/profile.component';
import { OrdersComponent } from './components/auth/my-account/orders/orders.component';
import { QuestionnairesComponent } from './components/auth/questionnaires/questionnaires.component';
import { QuestionnaireComponent } from './components/auth/questionnaire/questionnaire.component';
import { DashboardComponent } from './components/auth/dashboard/dashboard.component';
import { HelpComponent } from './components/auth/help/help.component';
import { TermsAndConditionsComponent } from './components/auth/terms-and-conditions/terms-and-conditions.component';
import { LegalComponent } from './components/auth/legal/legal.component';
import { TestsComponent } from './components/auth/tests/tests.component';
import { AdminComponent } from './components/admin/admin.component';
import { AdminLoginComponent } from './components/admin/admin-login/admin-login.component';
import { AdminGlossaryComponent } from './components/admin/admin-glossary/admin-glossary.component';
import { AdminGuard } from './guards/admin.guard';
import { AdminSurveyChoicesComponent } from './components/admin/admin-survey-choices/admin-survey-choices.component';
import { AdminSurveyAnswersComponent } from './components/admin/admin-survey-answers/admin-survey-answers.component';
import { FinalReportsComponent } from './components/auth/my-account/final-reports/final-reports.component';
import { ResourcesComponent } from './components/auth/resources/resources.component';
import { ResourceComponent } from './components/auth/resource/resource.component';
import { SingleReportComponent } from './components/auth/reports/single-report.component';
import { BillingInformationsComponent } from './components/auth/my-account/billing-informations/billing-informations.component';

const routes: Routes = [
  {
    path: 'admin',
    component: AdminComponent,
    children: [
      { path: '', component: AdminLoginComponent },
      {
        path: 'admin-panel',
        component: AdminPanelComponent,
        canActivate: [AdminGuard],
      },
      {
        path: 'admin-survey-choices',
        component: AdminSurveyChoicesComponent,
        canActivate: [AdminGuard],
      },
      {
        path: 'admin-survey-answers',
        component: AdminSurveyAnswersComponent,
        canActivate: [AdminGuard],
      },

      {
        path: 'admin-glossary',
        component: AdminGlossaryComponent,
        canActivate: [AdminGuard],
      },
    ],
  },
  {
    path: 'auth-wall',
    component: AuthWallComponent,
    children: [
      { path: '', component: LoginComponent },
      { path: 'forgot-password', component: ForgotPasswordComponent },
      { path: 'signup', component: SignupComponent },
    ],
  },

  {
    path: 'dashboard',
    component: AuthComponent,
    canActivate: [AuthGuard],
    children: [
      { path: '', component: DashboardComponent },

      { path: 'questionnaires', component: QuestionnairesComponent },
      { path: 'questionnaire/:id', component: QuestionnaireComponent },

      { path: 'resources', component: ResourcesComponent },
      { path: 'resource/:id', component: ResourceComponent },

      { path: 'reports', component: ReportsComponent },
      { path: 'report', component: SingleReportComponent },

      { path: 'help', component: HelpComponent },
      { path: 'terms-and-conditions', component: TermsAndConditionsComponent },
      { path: 'legal', component: LegalComponent },

      {
        path: 'my-account',
        component: MyAccountComponent,
        children: [
          { path: 'profile', component: ProfileComponent },
          { path: 'orders', component: OrdersComponent },
          {
            path: 'final-reports',
            component: FinalReportsComponent,
          },
          {
            path: 'billing-informations',
            component: BillingInformationsComponent,
          },
          {
            path: '**',
            redirectTo: 'profile',
          },
        ],
      },

      { path: 'tests', component: TestsComponent },
    ],
  },

  { path: '**', redirectTo: '/auth-wall' },
];
@NgModule({
  imports: [
    RouterModule.forRoot(routes, { scrollPositionRestoration: 'enabled' }),
  ],
  exports: [RouterModule],
})
export class AppRoutingModule {}
