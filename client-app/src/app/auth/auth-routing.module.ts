import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { AuthComponent } from './auth.component';
import { ForgotPasswordFormComponent } from './containers/forgot-password-form.component';
import { LoginFormComponent } from './containers/login-form.component';
import { SignupFormComponent } from './containers/signup-form.component';

const routes: Routes = [
  {
    path: '', component: AuthComponent, children: [
      {
        path: 'login', component: LoginFormComponent
      },
      {
        path: 'signup', component: SignupFormComponent
      },
      {

        path: 'forgot-password', component: ForgotPasswordFormComponent
      },
      {
        path: '**', redirectTo: 'login'
      }
    ]
  },

];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class AuthRoutingModule { }
