import { HttpClient } from '@angular/common/http';
import { AfterViewInit, Component, OnInit } from '@angular/core';
import { interval, Subject } from 'rxjs';
import { takeUntil, tap } from 'rxjs/operators';
import { environment } from 'src/environments/environment';

@Component({
  selector: 'app-dashboard',
  templateUrl: './dashboard.component.html',
  styleUrls: ['./dashboard.component.scss'],
})
export class DashboardComponent implements OnInit, AfterViewInit {
  destroy$ = new Subject<void>();

  currentSteps = [1, 1, 1, 1];
  nextInLine = 0;

  startBtnText = 'Débuter maintenant';
  nextSurveyID = 'B';

  completed = [false, false, false, false];

  constructor(private http: HttpClient) {}

  ngOnInit(): void {
    this.http
      .get<{ survey_id: string }>(environment.apiUrl + '/users_surveys/next', {
        observe: 'response',
      })
      .subscribe((res) => {
        if (!res.ok || !res.body) {
          return;
        }

        const nextSurveyID = res.body.survey_id;

        if (nextSurveyID !== 'B') {
          this.startBtnText = 'Continuer';
          this.nextSurveyID = nextSurveyID;
        }
      });
  }

  ngAfterViewInit() {
    interval(1000)
      .pipe(
        takeUntil(this.destroy$),
        tap(() => {
          if (this.currentSteps[3] === 3) {
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
