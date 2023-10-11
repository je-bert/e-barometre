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

  public getReportById(id: number): Observable<any> {
    return this.http.get(environment.apiUrl + '/results/', {
      responseType: 'text',
    });
  }
}
