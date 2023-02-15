import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable, of, timer } from 'rxjs';
import { map, catchError, tap } from 'rxjs/operators';

import { environment } from 'src/environments/environment';

@Injectable({
  providedIn: 'root',
})
export class AuthService {
  constructor(private http: HttpClient) {}

  login(loginDto: LoginDto): Observable<TokenOrNull> {
    return this.http
      .post<{ token: string | null }>(environment.apiUrl + '/auth/sign-in', {
        ...loginDto,
      })
      .pipe(
        map((res) => res.token),
        catchError(() => of(null)),
        tap((token) => {
          if (!token) return;

          window.localStorage.setItem('token', token);
        })
      );
  }

  signup(signupDto: Partial<SignupDto>): Observable<TokenOrNull> {
    return this.http
      .post<{ token: string | null }>(environment.apiUrl + '/auth/sign-up', {
        ...signupDto,
      })
      .pipe(
        map((res) => res.token),
        catchError(() => of(null)),
        tap((token) => {
          if (!token) return;
          window.localStorage.setItem('token', token);
        })
      );
  }

  logout() {
    window.localStorage.removeItem('token');

    return timer(350);
  }
}

type TokenOrNull = string | null;

interface LoginDto {
  email: string;
  password: string;
}

interface SignupDto {
  first_name: string;
  last_name: string;
  email: string;
  phone_number: string;
  password: string;
}
