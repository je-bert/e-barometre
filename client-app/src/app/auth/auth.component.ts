import { Component } from '@angular/core';

@Component({
  selector: 'app-auth',
  template: `
    <section class="tw-min-h-screen tw-bg-custom-pale-gray tw-flex">
      <div class="tw-w-full md:tw-w-1/2 tw-flex tw-items-center">
        <div class="tw-p-12">
          <div>
            <div>
              <router-outlet></router-outlet>
            </div>
          </div>
        </div>
      </div>
      <div
        class="
    tw-bg-no-repeat 
    tw-bg-cover 
    tw-bg-[url('/assets/img/blue_gradient_bg.png')] tw-hidden md:tw-flex md:tw-w-1/2 tw-items-center tw-justify-center"
      >
        <img src="/assets/img/logo_with_name.png" class="tw-h-1/3" />
      </div>
    </section>
  `,
  styles: [],
})
export class AuthComponent {}
