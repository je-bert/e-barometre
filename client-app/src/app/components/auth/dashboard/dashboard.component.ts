import { HttpClient } from '@angular/common/http';
import { AfterViewInit, Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { BehaviorSubject, EMPTY, interval, of, Subject } from 'rxjs';
import { map, mergeMap, takeUntil, tap } from 'rxjs/operators';
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

  startBtnText = 'Chargement...';
  nextSurveyID = 'B';

  completed = [false, false, false, false];

  constructor(private http: HttpClient, private router: Router) {}

  ngOnInit(): void {
    this.http
      .get<{ survey_id: string; message: string; user_id: string }>(
        environment.apiUrl + '/users_surveys/next',
        {
          observe: 'response',
        }
      )
      .pipe(
        mergeMap((response) => {
          if (response.body === null) {
            this.startBtnText = 'Acheter un forfait pour commencer';
            return of(null);
          }

          if (response.body.message === 'Done') {
            return this.http.post(environment.apiUrl + '/results/', {}).pipe(
              tap((res) => {
                this.startBtnText = 'Voir votre rapport';
              }),
              map(() => null)
            );
          }

          const nextSurveyID = response.body.survey_id;

          if (nextSurveyID === null) this.startBtnText = 'Voir votre rapport';

          return of(nextSurveyID);
        })
      )
      .subscribe((nextSurveyID) => {
        if (nextSurveyID === null) {
          return;
        }

        if (nextSurveyID !== 'B') {
          this.startBtnText = 'Continuer';
          this.nextSurveyID = nextSurveyID;
          return;
        }

        this.startBtnText = 'Débuter un nouveau questionnaire';
      });
  }

  handleNavigateToAnalysis() {
    this.router.navigate(['/dashboard/reports']);
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
