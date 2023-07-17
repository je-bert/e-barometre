import { Component, OnInit, ViewEncapsulation } from '@angular/core';
import { environment } from 'src/environments/environment';

import { HttpClient } from '@angular/common/http';

import { of, Subject } from 'rxjs';
import { tap, map, catchError, delay, concatMap } from 'rxjs/operators';

type Survey = {
  survey_id: string;
  name: string;
  description: string;
  status: string;
  cover_picture_url: string;
  color: string;
  index: number;
};

type Question = {
  condition: string;
  index: number;
  info_bubble_text: string;
  intensity: number;
  conditional_intensity: string;
  label_id: string;
  max_value: number;
  min_value: number;
  question_id: string;
  title: string;
  intro: string | null;
  type: string;
  choices: any[];
  ladderC: number;
  ladderE: number;
  ladderV: number;
  categorie: string;
  active: boolean;
  violence_related: boolean;
};

@Component({
  selector: 'app-admin-panel',
  templateUrl: './admin-panel.component.html',
  styleUrls: ['./admin-panel.component.scss'],
  encapsulation: ViewEncapsulation.None,
})
export class AdminPanelComponent implements OnInit {
  destroy$ = new Subject<void>();

  constructor(private http: HttpClient) {}

  editSurveyModalOpened = false;
  editQuestionModalOpened = false;

  isReloadingQuestionnaires = false;

  isReloadingSingleQuestionnaire = false;

  handleOpenQuestionnairesPanel() {
    this.surveyId = '';
  }

  public combinedLadderAbove100 = () => {
    return (
      this.editQuestionFormData.ladderC +
        this.editQuestionFormData.ladderE +
        this.editQuestionFormData.ladderV >
      100
    );
  };

  public isValidQuestionEdit = () => {
    return !this.combinedLadderAbove100();
  };

  surveyId = '';
  editSurveyId = '';

  editQuestionId = '';

  binaryChoices = [
    { value: '1', label: 'oui' },
    { value: '0', label: 'non' },
  ];

  editSurveyFormData = {} as Survey;

  editQuestionFormData = {} as Question;

  surveyQuestionCategories$ = this.http.get<{ category_id: string }[]>(
    environment.apiUrl + '/admin/survey-categories'
  );

  relatedConditional$ = of(null).pipe(
    concatMap(() =>
      this.http.get<any>(
        environment.apiUrl +
          '/admin/survey-related-conditional/' +
          this.editQuestionId
      )
    ),
    tap(console.log),
    tap(() => {
      console.log(this.editQuestionId);
    })
  );

  editSurvey$ = this.http.get<Survey[]>(environment.apiUrl + '/survey/').pipe(
    map((surveys) => {
      return surveys.filter(
        (survey) => survey.survey_id == this.editSurveyId
      )[0] as Survey;
    }),
    tap((survey) => (this.editSurveyFormData = survey))
  );

  editQuestion$ = of(null).pipe(
    concatMap(() =>
      this.http.get<Question>(
        environment.apiUrl + '/admin/question/' + this.editQuestionId
      )
    ),
    tap(console.log),
    tap((question) => (this.editQuestionFormData = question))
  );

  handleEditSurvey(surveyId: string) {
    this.editQuestionId = '';
    this.editQuestionModalOpened = false;

    this.editSurveyId = surveyId;
    this.editSurveyModalOpened = true;
  }

  handleEditQuestion(questionId: string) {
    this.editSurveyId = '';
    this.editSurveyModalOpened = false;

    this.editQuestionId = questionId;

    this.editQuestionModalOpened = true;
  }

  handleConfirmEditSurvey() {
    this.http
      .patch(
        environment.apiUrl + '/admin/surveys/' + this.editSurveyId,
        this.editSurveyFormData
      )
      .pipe(
        catchError((err) => {
          console.log(err);
          throw err;
        }),
        tap(() => {
          this.editSurveyId = '';
          this.editSurveyModalOpened = false;
          this.isReloadingQuestionnaires = true;
        }),
        delay(350),
        tap(() => {
          this.isReloadingQuestionnaires = false;
        })
      )
      .subscribe(console.log);
  }

  handleConfirmEditQuestion() {
    this.http
      .patch(
        environment.apiUrl + '/admin/question/' + this.editQuestionId,
        this.editQuestionFormData
      )
      .pipe(
        catchError((err) => {
          console.log(err);
          throw err;
        }),
        tap(() => {
          this.editQuestionId = '';
          this.editQuestionModalOpened = false;
          this.isReloadingSingleQuestionnaire = true;
        }),
        delay(350),
        tap(() => {
          this.isReloadingSingleQuestionnaire = false;
        })
      )
      .subscribe(console.log);
  }

  handleViewQuestions(surveyId: string) {
    this.surveyId = '';
    setTimeout(() => {
      this.surveyId = surveyId;
    }, 350);
  }

  ngOnInit(): void {}
}
