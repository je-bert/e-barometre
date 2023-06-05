import { Component, OnInit, Input, Output, EventEmitter } from '@angular/core';

import { ClientSideQuestion, QuestionAnswer } from 'src/app/models/question';

@Component({
  selector: 'app-numeric-ladder[question]',
  templateUrl: './numeric-ladder.component.html',
  styleUrls: ['./numeric-ladder.component.scss'],
})
export class NumericLadderComponent implements OnInit {
  @Input() question!: ClientSideQuestion;

  @Output() answerPicked = new EventEmitter<{
    question: ClientSideQuestion;
    answer: QuestionAnswer;
  }>();

  constructor() {}

  ngOnInit(): void {}
}
