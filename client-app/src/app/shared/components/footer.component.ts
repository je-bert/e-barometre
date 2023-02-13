import { Component } from '@angular/core';

@Component({
  selector: 'app-footer',
  template: `
 <footer style="background-color: #030d45" class="site-footer pt-5 pb-4">
  <div
    class="
      container
      d-md-flex
      justify-content-between
      align-items-center
      text-center
    "
  >
    <ul class="list-inline fs-sm mb-3 order-md-2">
      <li class="list-inline-item my-1">
        <a class="nav-link-style nav-link-light" 
          >Aide</a
        >
      </li>
      <li class="list-inline-item my-1">
        <a
          class="nav-link-style nav-link-light"
    
          >Conditions d'utlisation</a
        >
      </li>
      <li class="list-inline-item my-1">
        <a class="nav-link-style nav-link-light" 
          >Avis légal
        </a>
      </li>

      <li class="list-inline-item my-1">
        <a class="nav-link-style nav-link-light" 
          >Tests</a
        >
      </li>

      <li class="list-inline-item my-1">
        <a
          class="nav-link-style nav-link-light tw-cursor-pointer"

          >Déconnexion
        </a>
      </li>
    </ul>
    <p class="fs-sm mb-3 order-md-1">
      <span class="text-light opacity-50 me-1"
        >© Tous droits réservés. Produit par</span
      ><a class="nav-link-style nav-link-light">Carbonia Web</a>
    </p>
  </div>
</footer>
 
  `,
  styles: [
  ]
})
export class FooterComponent {

}
