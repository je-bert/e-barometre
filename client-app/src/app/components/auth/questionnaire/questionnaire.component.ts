import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';

import { QuestionsService } from 'src/app/services/questionnaire.service';

@Component({
  selector: 'app-questionnaire',
  templateUrl: './questionnaire.component.html',
  styleUrls: ['./questionnaire.component.scss'],
  providers: [QuestionsService],
})
export class QuestionnaireComponent implements OnInit {
  constructor(
    private route: ActivatedRoute,
    private questionsService: QuestionsService
  ) {}

  public getTitle() {
    return 'Questionnaire ' + this.questionsService.questionnaireName;
  }

  getQuestionnaireColor = () => this.questionsService.questionnaireColor;

  getQuestionnaireImage = () => this.questionsService.questionnaireImage;

  getCurrentCircleToFill = () => this.questionsService.getCurrentCircleToFill();

  public isStarted = false;

  public start(): void {
    this.isStarted = true;
  }

  public end(): void {
    this.isStarted = false;
  }

  public checkIfAlreadyStarted(): boolean {
    return this.questionsService.getProgress() !== '0%';
  }

  public checkIfMarkedAsCompleted(): boolean {
    return this.questionsService.getIsCompleted();
  }

  public getCallToActionButtonText(): string {
    if (this.checkIfAlreadyStarted()) {
      return 'Continuer';
    }

    return 'Commencer';
  }

  public getIsLoaded(): boolean {
    return this.questionsService.getQuestions().length > 0;
  }

  public submit(): void {
    this.questionsService.submitQuestionnaire();
  }

  ngOnInit(): void {
    this.route.params.subscribe((params) => {
      const questionnaireId = params['id'];
      this.questionsService.getSingleQuestionnaire(questionnaireId);
    });
  }
}
