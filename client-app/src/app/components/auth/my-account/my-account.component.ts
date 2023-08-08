import { Component } from '@angular/core';
import { Router } from '@angular/router';

@Component({
  selector: 'app-my-account',
  templateUrl: './my-account.component.html',
  styleUrls: ['./my-account.component.scss'],
})
export class MyAccountComponent {
  constructor(private router: Router) {}

  logout() {
    window.sessionStorage.removeItem('token');
    this.router.navigateByUrl('/auth-wall');
  }
}