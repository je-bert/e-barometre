import { Component } from '@angular/core';

@Component({
  selector: 'app-forgot-password-form',
  template: `
<!-- Sign in view-->
<div class="view show p-5" id="signin-view">
  <h1 class="h2 pb-3">Vous avez oublié votre mot de passe?</h1>
  <p class="">Obtenez un nouveau mot de passe en 3 étapes faciles.</p>
  <ul class="list-unstyled pb-1 mb-4">
    <li>
      <span class="text-primary fw-semibold me-1">1.</span>Entrez votre adresse
      courriel dans le champ ci-dessous.
    </li>
    <li>
      <span class="text-primary fw-semibold me-1">2.</span>Repérez le code
      envoyé dans vos courriels.
    </li>
    <li>
      <span class="text-primary fw-semibold me-1">3.</span>Entrez les 6 chiffres
      dans le champ prévu à cet effet.
    </li>
  </ul>
  <div class="bg-faded-primary rounded-3 px-3 py-4 p-sm-4">
    <form class="needs-validation p-2" novalidate>
      <div class="mb-3 pb-1">
        <label class="form-label" for="recovery-email"
          >Entrez votre adresse courriel</label
        >
        <input class="form-control" type="email" required id="recovery-email" />
        <div class="invalid-feedback">
          Veuillez svp entrer une adresse courriel valide!
        </div>
      </div>
      <button  class="btn btn-primary">
        Réinitialiser le mot de passe
      </button>
    </form>
  </div>
</div>

<div class="border-top text-center mt-4 pt-2">
  <p class="pt-3 mb-0 text-center">
    Vous n'avez pas encore de compte?
    <a routerLink="/auth/signup" class="fw-medium" data-view="#signup-view"
      >Inscrivez-vous</a
    >
  </p>
</div>
 
  `,
  styles: [
  ]
})
export class ForgotPasswordFormComponent {

}
