import { Component, OnInit, Input } from '@angular/core';
import { CommonModule } from '@angular/common';

import { MatIconModule } from '@angular/material/icon';
import { FormsModule } from '@angular/forms';
import { Report } from 'src/app/models/report';
import { Router } from '@angular/router';
import { ReportsService } from 'src/app/services/reports.service';
import { NotificationService } from 'src/app/services/notification.service';
import { ErrorResponse } from 'src/app/models/response';
import { HttpClient } from '@angular/common/http';
import { catchError } from 'rxjs';

@Component({
  selector: 'app-single-report-presentation[report]',
  standalone: true,
  imports: [CommonModule, MatIconModule, FormsModule],
  providers: [ReportsService, NotificationService],
  template: `
    <a class="card card-hover border-0 shadow tw-relative">
      <img
        class="card-img-top"
        src="/assets/img/portfolio/01.jpg"
        alt="Portfolio thumb"
      />
      <div class="card-body text-center bg-secondary">
        <h3 class="h5 nav-heading mb-2">
          <span *ngIf="!isEditing"> {{ report.name }} </span>

          <input
            class="form-control"
            type="text"
            *ngIf="isEditing"
            [(ngModel)]="report.name"
            name="name"
          />
        </h3>
        <p class="text-muted mb-2">
          complété le {{ formatDate(report.date_created) }}
        </p>
        <button
          (click)="openReportHTML(report.report_id)"
          class="mx-2 btn btn-primary"
        >
          Afficher le rapport
        </button>
        <button
          (click)="openReportPDF(report.report_id)"
          class="mx-2 btn btn-marie"
        >
          Télécharger PDF
        </button>
        <mat-icon (click)="onEdit()" class="tw-absolute tw-top-4 tw-right-4"
          >edit</mat-icon
        >
      </div>
    </a>
  `,
  styles: [],
})
export class SingleReportPresentationComponent implements OnInit {
  @Input() report!: Report;
  @Input() onCardClick!: (id: number) => void;

  isEditing = false;
  constructor(
    private http: HttpClient,
    private notificationService: NotificationService,
    private reportsService: ReportsService
  ) {}

  public openReportHTML(id: number) {
    this.reportsService
      .getReportHTMLById(id)
      .pipe(
        catchError((error) => {
          console.error('Error fetching HTML content:', error);
          this.notificationService.show({
            message: "Une erreur est survenue lors de l'ouverture du rapport",
            type: 'danger',
          });
          throw error;
        })
      )
      .subscribe((data) => {
        const blob = new Blob([data], { type: 'text/html' });
        const url = window.URL.createObjectURL(blob);

        const newWindow = window.open(url, '_blank');
        if (newWindow) {
          newWindow.focus();
        }
      });
  }

  public openReportPDF(id: number) {
    this.reportsService
      .getReportPDFById(id)
      .pipe(
        catchError((error) => {
          console.error('Error fetching PDF content:', error);
          this.notificationService.show({
            message: "Une erreur est survenue lors de l'ouverture du rapport",
            type: 'danger',
          });
          throw error;
        })
      )
      .subscribe((data) => {
        const blob = new Blob([data], { type: 'application/pdf' });
        const url = window.URL.createObjectURL(blob);

        window.open(url, '_blank')?.focus();
      });
  }
  onEdit() {
    this.isEditing = !this.isEditing;
  }

  formatDate(date: string) {
    const dateObj = new Date(date);
    return dateObj.toLocaleDateString('fr-CA', {
      year: 'numeric',
      month: 'short',
      day: 'numeric',
    });
  }

  ngOnInit(): void {}
}
