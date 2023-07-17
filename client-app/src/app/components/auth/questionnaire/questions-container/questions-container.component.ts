import { Component, Output, EventEmitter, Input } from '@angular/core';

import {
  ClientSideQuestion,
  QuestionAnswer,
} from '../../../../models/question';

import { QuestionsService } from 'src/app/services/questionnaire.service';

@Component({
  selector: 'app-questions-container[questionnaireColor]',
  templateUrl: './questions-container.component.html',
  styleUrls: ['./questions-container.component.scss'],
})
export class QuestionsContainerComponent {
  constructor(private questionsService: QuestionsService) {}

  public shouldShowSaveAlert = false;

  @Input() questionnaireColor!: string;

  @Output() questionnaireEnd = new EventEmitter();

  @Output() questionnaireSubmit = new EventEmitter();

  submit() {
    this.questionnaireSubmit.emit();
  }

  getQuestions(): ClientSideQuestion[] {
    return this.questionsService.getQuestions();
  }

  getProgress(): string {
    return this.questionsService.getProgress();
  }

  onInfoBubbleOpen(question: ClientSideQuestion): void {
    this.questionsService.onInfoBubbleToggle(question);
  }

  public isDone(): boolean {
    return this.questionsService.isDone();
  }

  onSave(): void {
    this.questionsService.onSave();

    this.shouldShowSaveAlert = true;

    setTimeout(() => {
      this.shouldShowSaveAlert = false;
    }, 2000);
  }

  onSkip(question: ClientSideQuestion): void {
    this.questionsService.onSkip(question);
  }

  onReset(): void {
    this.questionsService.reset();
  }

  onToggleConfirm(question: ClientSideQuestion): void {
    this.questionsService.onToggleConfirm(question);
  }

  markAsCompleted(): void {
    this.questionsService.onSave();
    this.questionnaireEnd.emit();
  }

  public getHasCannotSkipLastError(): boolean {
    return this.questionsService.showCannotSkipLastQuestionWarning;
  }

  onAnswer({
    question,
    answer,
  }: {
    question: ClientSideQuestion;
    answer: QuestionAnswer;
  }): void {
    this.questionsService.onAnswer(question, answer);
  }
}
