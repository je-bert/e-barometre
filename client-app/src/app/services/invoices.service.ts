import { Injectable } from '@angular/core';
import { environment } from 'src/environments/environment';

import { HttpClient } from '@angular/common/http';
import { Router } from '@angular/router';

import { Observable } from 'rxjs';
import { Invoice } from '../models/invoice';

@Injectable()
export class InvoicesService {
  constructor(private http: HttpClient, private router: Router) {}

  public getAllInvoices(): Observable<Invoice[]> {
    return this.http.get<Invoice[]>(environment.apiUrl + '/invoices/');
  }

  public getInvoiceById(id: number): Observable<Invoice> {
    return this.http.get<Invoice>(environment.apiUrl + '/invoices/' + id);
  }

  public getPublishableKey(): Observable<any> {
    return this.http.get<any>(environment.apiUrl + '/stripe/publishable-key');
  }
}
