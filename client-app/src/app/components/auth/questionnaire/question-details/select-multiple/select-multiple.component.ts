import { Component, OnInit, Input, Output, EventEmitter } from '@angular/core';

import { ClientSideQuestion, QuestionAnswer } from 'src/app/models/question';

@Component({
  selector: 'app-select-multiple',
  templateUrl: './select-multiple.component.html',
  styleUrls: ['./select-multiple.component.scss'],
})
export class SelectMultipleComponent implements OnInit {
  @Input() question!: ClientSideQuestion;

  @Output() answerPicked = new EventEmitter<{
    question: ClientSideQuestion;
    answer: QuestionAnswer;
  }>();

  constructor() {}

  ngOnInit(): void {}
}
