import { HttpClient } from '@angular/common/http';
import { Component } from '@angular/core';
import { Router } from '@angular/router';
import { AuthService } from '../services/auth.service';

@Component({
  selector: 'app-login-form',
  template: `

<div class="view show p-0 p-md-5" id="signin-view">
  <h2>Connexion</h2>

  <p class="mt-3 mb-4">
    Veuillez entrer votre adresse courriel et votre mot de passe afin de vous
    connecter.
  </p>
  <form
  #loginForm="ngForm"
  (ngSubmit)="handleSubmit()"
  novalidate
 
    class="needs-validation w-full"
  >
    <div class="input-group mb-3 w-full">
      <i
        class="ai-mail position-absolute top-50 start-0 translate-middle-y ms-3"
      ></i>
      <input
        class="form-control rounded tw-w-full"
        type="email"
        placeholder="Email"
        required
        [(ngModel)]="loginFormData.email"
 
        name="email"
      />
    </div>
    <div class="input-group mb-3">
      <i
        class="ai-lock position-absolute top-50 start-0 translate-middle-y ms-3"
      ></i>
      <div class="password-toggle w-100 w-full">
        <input
          class="form-control mb-2 w-full"
          [type]="isPasswordMasked ? 'password' : 'text'"
          placeholder="Password"
          required
          name='password'
          [(ngModel)]="loginFormData.password"
        />
        <label class="password-toggle-btn" aria-label="Show/hide password">
          <input (click)="togglePasswordMasked()" class="password-toggle-check" type="checkbox" /><span
            class="password-toggle-indicator"
          ></span>
        </label>
      </div>
    </div>

    <button
      class="btn btn-primary d-block w-100 mt-5 mb-2"
      [disabled]="!loginForm.form.valid"

    >
      SE CONNECTER
    </button>
    <p class="pt-3 mb-0 text-center">
      Mot de passe oublié?
      <a
        routerLink="/auth/forgot-password"
        class="fw-medium tw-text-primary"
        data-view="#signup-view"
        >Cliquez ici.</a
      >
    </p>
  </form>
</div>

<div class="border-top text-center mt-4 pt-2">
  <p class="pt-3 mb-0 text-center">
    Vous n'avez pas encore de compte?
    <a
      routerLink="/auth/signup"
      class="fw-medium tw-text-primary"
      data-view="#signup-view"
      >Inscrivez-vous</a
    >
  </p>
</div>
 
  `,
  styles: [``
  ]
})
export class LoginFormComponent {

  loginFormData: LoginFormData = {
    email: null,
    password: null,
  }

  isPasswordMasked = true;





  constructor(private authService: AuthService, private router: Router) { }

  togglePasswordMasked() {
    this.isPasswordMasked = !this.isPasswordMasked; // TODO (simon) -> sync with css
  }

  handleSubmit() {

    this.login({ email: this.loginFormData.email!, password: this.loginFormData.password! })
  }



  private login({ email, password }: { email: string; password: string }) {
    this.authService.login({ email, password }).subscribe(token => {
      if (token === null) return;

      this.router.navigateByUrl('/surveys/demo')
    })
  }

}

interface LoginFormData {
  email: string | null;
  password: string | null;

}
