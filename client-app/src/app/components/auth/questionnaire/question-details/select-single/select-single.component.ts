import { Component, OnInit, Input, Output, EventEmitter } from '@angular/core';

import { ClientSideQuestion, QuestionAnswer } from 'src/app/models/question';

@Component({
  selector: 'app-select-single[question]',
  templateUrl: './select-single.component.html',
  styleUrls: ['./select-single.component.scss'],
})
export class SelectSingleComponent implements OnInit {
  @Input() question!: ClientSideQuestion;

  @Output() answerPicked = new EventEmitter<{
    question: ClientSideQuestion;
    answer: QuestionAnswer;
  }>();
  constructor() {}

  ngOnInit(): void {}
}
