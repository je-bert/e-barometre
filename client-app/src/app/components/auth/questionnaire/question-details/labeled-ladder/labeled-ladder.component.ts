import { Component, OnInit, Input, Output, EventEmitter } from '@angular/core';

import { ClientSideQuestion, QuestionAnswer } from 'src/app/models/question';

@Component({
  selector: 'app-labeled-ladder[question]',
  templateUrl: './labeled-ladder.component.html',
  styleUrls: ['./labeled-ladder.component.scss'],
})
export class LabeledLadderComponent implements OnInit {
  @Input() question!: ClientSideQuestion;

  @Output() answerPicked = new EventEmitter<{
    question: ClientSideQuestion;
    answer: QuestionAnswer;
  }>();

  constructor() {}

  ngOnInit(): void {}
}
