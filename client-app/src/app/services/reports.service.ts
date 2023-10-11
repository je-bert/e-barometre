import { Injectable } from '@angular/core';
import { environment } from 'src/environments/environment';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { Report } from '../models/report';

@Injectable()
export class ReportsService {
  constructor(private http: HttpClient) {}

  public getAllReports(): Observable<Report[]> {
    return this.http.get<Report[]>(environment.apiUrl + '/reports/');
  }
}
