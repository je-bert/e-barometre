import { HttpClient } from '@angular/common/http';
import { Component, OnInit } from '@angular/core';
import { environment } from 'src/environments/environment';

import { tap, map } from 'rxjs/operators';

@Component({
  selector: 'app-admin-answers',
  templateUrl: './admin-answers.component.html',
  styleUrls: ['./admin-answers.component.scss'],
})
export class AdminAnswersComponent implements OnInit {
  constructor(private http: HttpClient) {}

  answers$ = this.http.get(environment.apiUrl + '/admin/answers').pipe(
    tap(console.log),
    map((answers) => {
      return answers.map(
        (answer: {
          question_id: string;
          user_id: string;
          value: string;
          date_created: string;
        }) => {
          return {
            id: answer.question_id,
            value: answer.value,
          };
        }
      );
    }),
    tap(console.log)
  );

  ngOnInit(): void {}
}
