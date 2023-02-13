import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';

import { AuthRoutingModule } from './auth-routing.module';
import { AuthComponent } from './auth.component';
import { LoginFormComponent } from './containers/login-form.component';
import { SignupFormComponent } from './containers/signup-form.component';
import { ForgotPasswordFormComponent } from './containers/forgot-password-form.component';



@NgModule({
  declarations: [
    AuthComponent,
    LoginFormComponent,
    SignupFormComponent,
    ForgotPasswordFormComponent,

  ],
  imports: [
    CommonModule,
    AuthRoutingModule,
    FormsModule
  ]
})
export class AuthModule { }
