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

  public getReportHTMLById(id: number): Observable<string> {
    return this.http.get(environment.apiUrl + '/reports/' + id + '/html', {
      responseType: 'text',
    });
  }

  public getReportPDFById(id: number): Observable<ArrayBuffer> {
    return this.http.get(environment.apiUrl + '/reports/' + id + '/pdf', {
      responseType: 'arraybuffer',
    });
  }
}
