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
  public setPassword() {}
  public updateAccount() {}

  public deleteAccount() {
    return this.http.delete(environment.apiUrl + '/account/'); //TODO Kui Hua - Should I add error handling here?
  }
}
