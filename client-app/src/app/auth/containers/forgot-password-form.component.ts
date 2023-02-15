import { Component } from '@angular/core';

@Component({
  selector: 'app-forgot-password-form',
  template: `
    <div class="view show p-5 tw-bg-white">
      <h2 class="h2 pb-3">Vous avez oublié votre mot de passe?</h2>
      <p class="">Obtenez un nouveau mot de passe en 3 étapes faciles.</p>
      <ul class="list-unstyled pb-1 mb-4">
        <li>
          <span class="text-primary fw-semibold me-1">1.</span>Entrez votre
          adresse courriel dans le champ ci-dessous.
        </li>
        <li>
          <span class="text-primary fw-semibold me-1">2.</span>Repérez le code
          envoyé dans vos courriels.
        </li>
        <li>
          <span class="text-primary fw-semibold me-1">3.</span>Entrez les 6
          chiffres dans le champ prévu à cet effet.
        </li>
      </ul>
      <div class="tw-bg-[#aadbfc26] rounded-3 px-3 py-4 p-sm-4">
        <form
          novalidate=""
          class="needs-validation p-2 ng-untouched ng-pristine ng-valid"
        >
          <div class="mb-3 pb-1">
            <label
              for="recovery-email"
              class="form-label tw-pl-0 tw-font-bold tw-text-center tw-w-full mb-3"
              ng-reflect-for-attr="recovery-email"
              >Entrez votre adresse courriel</label
            ><input
              type="email"
              required=""
              id="recovery-email"
              class="form-control"
            />
            <div class="invalid-feedback">
              Veuillez svp entrer une adresse courriel valide!
            </div>
          </div>
          <div class="tw-flex tw-justify-center">
            <button type="submit" class="btn btn-primary mt-3" tabindex="0">
              Réinitialiser le mot de passe
            </button>
          </div>
        </form>
      </div>
    </div>

    <div class="border-top text-center mt-4 pt-2">
      <p class="pt-3 mb-0 text-center">
        Vous n'avez pas encore de compte?
        <a class="fw-medium tw-text-primary" routerLink="/auth/signup"
          >Inscrivez-vous</a
        >
      </p>
    </div>
  `,
  styles: [],
})
export class ForgotPasswordFormComponent {}
