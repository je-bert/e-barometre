import { Component, OnInit } from '@angular/core';

import { Questionnaire } from 'src/app/models/questionnaire';
import { QuestionsService } from 'src/app/services/questionnaire.service';

import { Observable, tap } from 'rxjs';

@Component({
  selector: 'app-questionnaires',
  templateUrl: './questionnaires.component.html',
  styleUrls: ['./questionnaires.component.scss'],
  providers: [QuestionsService],
})
export class QuestionnairesComponent implements OnInit {
  public questionnaires$: Observable<Questionnaire[]> | undefined;

  constructor(private questionsService: QuestionsService) {}

  public getQuestionnaires(): void {
    this.questionnaires$ = this.questionsService.getAllQuestionnaires();
    this.questionnaires$.pipe(tap(console.log));
  }

  ngOnInit(): void {
    this.getQuestionnaires();
  }
}
