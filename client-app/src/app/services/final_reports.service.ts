import { Injectable } from '@angular/core';
import { environment } from 'src/environments/environment';

import { HttpClient } from '@angular/common/http';
import { Router } from '@angular/router';

import { Observable } from 'rxjs';

@Injectable()
export class FinalReportService {
  constructor(private http: HttpClient, private router: Router) {}

  public getPublishableKey(): Observable<any> {
    return this.http.get<any>(environment.apiUrl + '/stripe/publishable-key');
  }

  public getSessionId(reportType: String, email: String): Observable<any> {
    return this.http.post(
      environment.apiUrl + '/stripe/create-checkout-session',
      { productId: reportType, email: email, app: true }
    );
  }
}
