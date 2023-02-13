import { Component } from '@angular/core';
import { Router } from '@angular/router';
import { AuthService } from '../services/auth.service';

@Component({
  selector: 'app-signup-form',
  template: `
 <!-- Sign in view-->
<div class="view show p-2" id="signin-view">
  <div class="">
    <h2>Inscrivez-vous!</h2>
    <p class="mt-3">Cela prendra moins d'une minute!</p>
    <form
      class="row needs-validation"

      (ngSubmit)="handleSubmit()"
      signupForm="#ngForm"
    >
      <div class="col-sm-6 mb-3">
        <label class="form-label" for="reg-fn"
          >Prénom<sup class="text-danger ms-1">*</sup></label
        >
        <input
          name="first name"
          class="form-control"
          type="text"
          required
        />
        <div class="invalid-feedback">Please enter you first name!</div>
      </div>
      <div class="col-sm-6 mb-3">
        <label class="form-label" for="reg-ln"
          >Nom de famille<sup class="text-danger ms-1">*</sup></label
        >
        <input
          name="last name"
          class="form-control"
          type="text"
          required=""
        />
        <div class="invalid-feedback">Please enter you last name!</div>
      </div>
      <div class="col-sm-6 mb-3">
        <label class="form-label" for="reg-email"
          >Courriel<sup class="text-danger ms-1">*</sup></label
        >
        <input
          name="email"
          class="form-control"
          type="email"
          required
          [(ngModel)]="signupFormData.email"
        />
        <div class="invalid-feedback">Please enter a valid email address!</div>
      </div>
      <div class="col-sm-6 mb-3">
        <label class="form-label" for="reg-phone">Téléphone</label>
        <input
          name="phone number"
          class="form-control bg-image-0"
          type="text"

        />
      </div>
      <div class="col-sm-6 mb-3">
        <label class="form-label" for="reg-password"
          >Mot de passe<sup class="text-danger ms-1">*</sup></label
        >
        <input
          name="password"
          class="form-control"
          type="password"
          required=""

          [(ngModel)]="signupFormData.password"
        />
        <div class="invalid-feedback">Please provide password!</div>
      </div>
      <div class="col-sm-6 mb-3">
         <label class="form-label" for="reg-confirm-password"
          >Confirm password<sup class="text-danger ms-1">*</sup></label
        >
        <input
          name="confirm password"
          class="form-control"
          type="password"
          required=""
          id="reg-confirm-password"
        />
        <div class="invalid-feedback">Password doesn't match!</div>
        
      </div>
      <div class="d-flex justify-content-between align-items-center mb-3 pb-1 tw-mt-4">
      <div class="form-check">
        <input class="form-check-input" type="checkbox"  required [(ngModel)]='signupFormData.consent' name='consent' />
        <label class="form-check-label" for="keep-signed-2"
          >J'accepte les termes et les conditions d'utlisations stipulées
          ci-dessous.</label
        >
      </div>
    </div>
      <div class="col-sm-6 pt-3">
        <button
       
          class="btn btn-primary d-block w-100"
        >
          S'inscrire
        </button>
      </div>
    </form>
    <div class="border-top text-center mt-4 pt-2">
      <p class="pt-3 mb-0 text-center">
         Déjà un compte? 
         <a routerLink="/auth/login" class="fw-medium tw-text-primary" >
           Connectez-vous
          </a>
        </p>
      </div>
  </div>
</div>
 
  `,
  styles: [
  ]
})
export class SignupFormComponent {

  signupFormData: SignupFormData = {

    email: null,
    lastName: null,
    firstName: null,
    phoneNumber: null,
    password: null,
    confirmPassword: null,
    consent: null,
  }

  constructor(private authService: AuthService, private router: Router) { }

  handleSubmit() {

    this.signup({
      email: this.signupFormData.email!,
      password: this.signupFormData.password!
    })
  }

  signup({ email, password }: { email: string; password: string }) {
    this.authService.signup({ email, password }).subscribe(token => {
      if (token === null) return;

      this.router.navigateByUrl('/surveys/demo')


    })
  }

  private arePasswordsMatching() {
    return this.signupFormData.password === this.signupFormData.confirmPassword
  }
}

interface SignupFormData {
  email: string | null;
  lastName: string | null;
  firstName: string | null;
  phoneNumber: string | null;
  password: string | null;
  confirmPassword: string | null;
  consent: boolean | null;
}
