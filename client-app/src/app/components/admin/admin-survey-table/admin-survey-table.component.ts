import { Component, EventEmitter, Output, Input } from '@angular/core';

import { ClrDatagridStateInterface } from '@clr/angular';

import { HttpClient } from '@angular/common/http';

import { tap } from 'rxjs/operators';
import { environment } from 'src/environments/environment';

type Survey = {
  color: string;
  cover_picture_url: string;
  description: string;
  index: number;
  name: string;
  status: string;
  survey_id: string;
};

type Question = {
  condition: string;
  index: number;
  intro: string | null;
  info_bubble_text: string;
  intensity: number;
  conditional_intensity: string;
  label_id: string;
  max_value: number;
  min_value: number;
  question_id: string;
  title: string;
  type: string;
  choices: any[];
  ladderC: number;
  ladderE: number;
  ladderV: number;
  category?: string;
};

@Component({
  selector: 'app-admin-survey-table',
  templateUrl: './admin-survey-table.component.html',
  styleUrls: ['./admin-survey-table.component.scss'],
})
export class AdminSurveyTableComponent {
  constructor(private http: HttpClient) {}

  @Output() onEditQuestion = new EventEmitter<string>();

  @Input() surveyId!: string;

  handleEditQuestion(questionId: string) {
    this.onEditQuestion.emit(questionId);
  }

  binaryChoices = [
    { value: '1', label: 'oui' },
    { value: '0', label: 'non' },
  ];

  panelOpenState = false;

  surveys: Survey[] = [];
  total = 0;
  loading = true;
  questions: Question[] = [];

  selectedSurvey: Survey | null = null;

  refresh(state: ClrDatagridStateInterface) {
    this.loading = true;
    // We convert the filters from an array to a map,
    // because that's what our backend-calling service is expecting
    let filters: { [prop: string]: any[] } = {};
    if (state.filters) {
      for (let filter of state.filters) {
        let { property, value } = <{ property: string; value: string }>filter;
        filters[property] = [value];
      }
    }

    this.http
      .get(environment.apiUrl + '/admin/surveys/' + this.surveyId)
      .pipe(tap(console.log))
      .subscribe((data) => {
        this.questions = data.questions;
        this.total = data.questions.length;
        this.loading = false;
      });
  }
}
