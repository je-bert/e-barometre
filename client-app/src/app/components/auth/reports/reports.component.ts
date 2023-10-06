import { Component, OnInit } from '@angular/core';
import { Observable, tap } from 'rxjs';
import { Report } from 'src/app/models/report';
import { ReportsService } from 'src/app/services/reports.service';

@Component({
  selector: 'app-reports',
  templateUrl: './reports.component.html',
  styleUrls: ['./reports.component.scss'],
  providers: [ReportsService],
})
export class ReportsComponent implements OnInit {
  public reports$: Observable<Report[]> | undefined;
  constructor(private reportsService: ReportsService) {}

  public getReports(): void {
    this.reports$ = this.reportsService.getAllReports();
    this.reports$.pipe(tap(console.log));
  }

  ngOnInit(): void {
    this.getReports();
  }
}
