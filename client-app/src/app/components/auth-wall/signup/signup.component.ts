import { Component } from '@angular/core';

import { environment } from 'src/environments/environment';

import { HttpClient } from '@angular/common/http';

import { Router } from '@angular/router';

@Component({
  selector: 'app-signup',
  templateUrl: './signup.component.html',
  styleUrls: ['./signup.component.scss'],
})
export class SignupComponent {
  public email = '';
  public lastName = '';
  public firstName = '';
  public phoneNumber = '';
  public password = '';
  public confirmPassword = '';

  public accountCreated = false;
  public passwordMatch(): boolean {
    return this.password === this.confirmPassword;
  }

  constructor(private router: Router, private http: HttpClient) {}

  signup() {
    // todo: add validation
    // if (!this.passwordMatch()) {
    //   alert('Passwords do not match');
    //   return;
    // }

    this.http
      .post<{ token: string }>(
        environment.apiUrl + '/auth/sign-up',

        {
          first_name: this.firstName,
          last_name: this.lastName,
          email: this.email,
          phone_number: this.phoneNumber,
          password: this.password,
        },
        { observe: 'response' }
      )

      .subscribe((res) => {
        if (!res.body || !res.body.token) return;

        this.accountCreated = true;
        window.sessionStorage.setItem('token', res.body.token);

        this.router.navigateByUrl('/dashboard');
      });
  }
}
