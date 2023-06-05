import { Component, OnInit, Input } from '@angular/core';
import { CommonModule } from '@angular/common';

import { MatIconModule } from '@angular/material/icon';
import { FormsModule } from '@angular/forms';

@Component({
  selector: 'app-single-report-presentation[name]',
  standalone: true,
  imports: [CommonModule, MatIconModule, FormsModule],
  template: `
    <a class="card card-hover border-0 shadow tw-relative"
      ><img
        class="card-img-top"
        src="/assets/img/portfolio/01.jpg"
        alt="Portfolio thumb"
      />
      <div class="card-body text-center bg-secondary">
        <h3 class="h5 nav-heading mb-2">
          <span *ngIf="!isEditing"> {{ name }} </span>

          <input
            class="form-control"
            type="text"
            *ngIf="isEditing"
            [(ngModel)]="name"
            name="name"
          />
        </h3>
        <p class="text-muted mb-2">complété le 2020/09/12</p>
        <button class="mx-2 btn btn-primary">Sommaire</button>
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
  @Input() name!: string;

  isEditing = false;

  constructor() {}

  onEdit() {
    this.isEditing = !this.isEditing;
  }

  ngOnInit(): void {}
}
