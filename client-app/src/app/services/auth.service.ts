import { Injectable } from '@angular/core';
import { Router } from '@angular/router';
import { environment } from 'src/environments/environment';
import { HttpClient } from '@angular/common/http';
import { NotificationService } from './notification.service';

@Injectable({ providedIn: 'root' })
export class AuthService {
	constructor(private router: Router, private http: HttpClient, private notificationService: NotificationService) {}

	public login(email: string, password: string, conditions: boolean) {
		this.http
      .post<{ token: string }>(
        environment.apiUrl + '/auth/sign-in',
        {
          email,
          password,
          conditions
        },
        { observe: 'response' }
      )
			.subscribe({
				next: (res) => {
					if (res.status === 200 && res.body) {
            window.sessionStorage.setItem('token', res.body.token);
            this.router.navigateByUrl('/dashboard');
          }
				},
				error: (error) => {
					this.notificationService.show({
						message: error.error,
						type: 'warning',
					});
				}
			});
	}
}