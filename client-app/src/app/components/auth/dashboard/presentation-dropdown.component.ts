import {
  ChangeDetectionStrategy,
  Component,
  Input,
  OnInit,
} from '@angular/core';
import { CommonModule } from '@angular/common';
import { MatIconModule } from '@angular/material/icon';
import { BehaviorSubject } from 'rxjs';

@Component({
  selector: 'app-presentation-dropdown[title][description]',
  standalone: true,
  changeDetection: ChangeDetectionStrategy.OnPush,
  imports: [CommonModule, MatIconModule],
  template: `
    <div (click)="onClick()" class="card h-100 border-0 shadow-lg">
      <div
        class="card-body text-center tw-p-5 tw-overflow-hidden tw-transition-[height] tw-duration-1000 tw-ease-in-out"
        [ngStyle]="{
          height: (isOpen$ | async) ? '125px' : '70px'
        }"
      >
        <h3 class="h6 mb-0">
          {{ title }}
          <mat-icon *ngIf="isOpen$ | async" style="transform: translateY(25%)"
            >expand_less</mat-icon
          >
          <mat-icon
            *ngIf="!(isOpen$ | async)"
            style="transform: translateY(25%)"
            >expand_more</mat-icon
          >
        </h3>
        <p class="tw-mb-0 tw-mt-4 tw-w-[300px]">
          {{ description }}
        </p>
      </div>
    </div>
  `,
  styles: [],
})
export class PresentationDropdownComponent implements OnInit {
  @Input() title!: string;
  @Input() description!: string;
  @Input() delay = 0;

  isOpen$ = new BehaviorSubject(false);

  constructor() {}

  onClick() {
    this.isOpen$.next(!this.isOpen$.getValue());
  }

  ngOnInit(): void {
    setTimeout(() => {
      this.isOpen$.next(true);
    }, this.delay);
  }
}
