import { AfterViewInit, Component, OnInit } from '@angular/core';
import { interval, Subject } from 'rxjs';
import { takeUntil, tap } from 'rxjs/operators';

@Component({
  selector: 'app-dashboard',
  templateUrl: './dashboard.component.html',
  styleUrls: ['./dashboard.component.scss'],
})
export class DashboardComponent implements OnInit, AfterViewInit {
  destroy$ = new Subject<void>();

  currentSteps = [1, 1, 1, 1];
  nextInLine = 0;

  completed = [false, false, false, false];

  constructor() {}

  ngOnInit(): void {}

  ngAfterViewInit() {
    interval(1000)
      .pipe(
        takeUntil(this.destroy$),
        tap(() => {
          if (this.currentSteps[3] === 4) {
            this.currentSteps = [1, 1, 1, 1];
            this.nextInLine = 0;
            return;
          }

          this.currentSteps[this.nextInLine] += 1;
          this.nextInLine = (this.nextInLine + 1) % 4;
        })
      )
      .subscribe();
  }
}
