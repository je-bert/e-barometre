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
          (click)="openReport(report.report_id)"
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

  isEditing = false;

  public openReport(id: number) {
    window.open('http://localhost:3000/api/results/1', '_blank'); // TODO: Real id + verify auth
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
