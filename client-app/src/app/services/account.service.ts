import { Injectable } from '@angular/core';
import { environment } from 'src/environments/environment';

import { HttpClient } from '@angular/common/http';
import { Router } from '@angular/router';

import { Observable } from 'rxjs';
import { Account } from '../models/account';

@Injectable()
export class AccountService {
  constructor(private http: HttpClient, private router: Router) {}

  public getAccount(): Observable<Account> {
    return this.http.get<Account>(environment.apiUrl + '/account/');
  }

  public setPassword(currentPassword: String, newPassword: String) {
    return this.http.patch(environment.apiUrl + '/account/set-password', {
      new_password: newPassword,
      current_password: currentPassword,
    });
  }

  public updateAccount() {}

  public deleteAccount() {
    return this.http.delete(environment.apiUrl + '/account/');
  }
}
