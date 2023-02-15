import { Component } from '@angular/core';

@Component({
  selector: 'app-navbar',
  template: `
    <header
      class="
    header
    navbar navbar-expand-lg navbar-dark navbar-floating navbar-sticky
  "
    >
      <div class="container px-0 px-xl-3">
        <button class="navbar-toggler ms-n2 me-2">
          <span class="navbar-toggler-icon"></span></button
        ><a class="navbar-brand flex-shrink-0 order-lg-1 mx-auto ms-lg-0"
          ><img
            class="navbar-floating-logo d-none d-lg-block"
            src="/assets/img/logo.png"
            style="filter: brightness(0) invert(1)"
            alt="Logo"
            width="153" />

          <img
            class="d-lg-none"
            src="/assets/img/logo_constellation_icon.png"
            width="58"
        /></a>
        <div class="d-flex align-items-center order-lg-3 ms-lg-auto">
          <div class="navbar-tool tw-cursor-pointer">
            <span class="navbar-tool-icon-box">
              <img
                class="navbar-tool-icon-box-img"
                src="/assets/img/demo_avatar.jpg"
                alt="Avatar"
              />
            </span>
            <span class="navbar-tool-label">
              <small>Bonjour,</small>
              Amanda</span
            >
          </div>
        </div>
        <div class="offcanvas offcanvas-collapse order-lg-2" id="primaryMenu">
          <div class="offcanvas-header navbar-shadow">
            <h5 class="mt-1 mb-0">Menu</h5>
            <button
              class="btn-close lead"
              type="button"
              data-bs-dismiss="offcanvas"
              aria-label="Close"
            ></button>
          </div>
          <div class="offcanvas-body justify-content-center">
            <!-- Menu-->
            <ul class="navbar-nav">
              <li class="nav-item">
                <a class="nav-link">Tableau de bord</a>
              </li>
              <li class="nav-item">
                <a class="nav-link">Ressources</a>
              </li>

              <li class="nav-item">
                <a class="nav-link">Rapports</a>
              </li>
            </ul>
          </div>
        </div>
      </div>
    </header>
  `,
  styles: [],
})
export class NavbarComponent {}
