import { Component } from '@angular/core';

import { environment } from 'src/environments/environment';

import { Router } from '@angular/router';
import { HttpClient } from '@angular/common/http';
import { NotificationService } from 'src/app/services/notification.service';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.scss'],
})
export class LoginComponent {
  public email = '';
  public password = '';
  public showPassword = false;

  constructor(
    private router: Router,
    private http: HttpClient,
    private notificationService: NotificationService
  ) {}

  public onPasswordToggleChange(event: Event) {
    const checked = (event.target as HTMLInputElement).checked;
    this.showPassword = checked;
  }

  login() {
    this.http
      .post<{ token: string }>(
        environment.apiUrl + '/auth/sign-in',
        {
          email: this.email,
          password: this.password,
        },
        { observe: 'response' }
      )
      .subscribe({
        next: (res) => {
          if (res.status === 200 && res.body) {
            window.sessionStorage.setItem('token', res.body.token);
            this.router.navigateByUrl('/dashboard');
            return;
          }
        },

        error: (error) => {
          this.notificationService.show({
            message: error.error,
            type: 'warning',
          });
        },
      });
  }
}
