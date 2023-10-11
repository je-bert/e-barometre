import { Component, OnInit, Input } from '@angular/core';
import { CommonModule } from '@angular/common';

import { MatIconModule } from '@angular/material/icon';
import { FormsModule } from '@angular/forms';
import { Report } from 'src/app/models/report';
import { Router } from '@angular/router';
import { ReportsService } from 'src/app/services/reports.service';
import { NotificationService } from 'src/app/services/notification.service';
import { ErrorResponse } from 'src/app/models/response';

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
          (click)="getReport(report.report_id)"
          class="mx-2 btn btn-primary"
        >
          Sommaire
        </button>
        <button class="mx-2 btn btn-marie">Complet</button>
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
  innerHTML: string;

  constructor(
    private router: Router,
    private reportsService: ReportsService,
    private notificationService: NotificationService
  ) {}

  isEditing = false;

  public getReport(id: number) {
    this.reportsService.getReportById(id).subscribe({
      next: (text: string) => {
        //this.innerHTML = text;
        // TODO: Display html in a modal
      },
      error: (response: ErrorResponse) => {
        this.notificationService.show({
          message: `${response.error.message}`,
          type: 'danger',
        });
      },
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
