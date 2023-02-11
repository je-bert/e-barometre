import { Component, OnInit, Input, Output, EventEmitter } from '@angular/core';

import { ClientSideQuestion, QuestionAnswer } from 'src/app/models/question';

@Component({
  selector: 'app-integer',
  templateUrl: './integer.component.html',
  styleUrls: ['./integer.component.scss'],
})
export class IntegerComponent implements OnInit {
  @Input() questionnaireColor!: string;

  @Input() question!: ClientSideQuestion;

  @Output() answerPicked = new EventEmitter<{
    question: ClientSideQuestion;
    answer: QuestionAnswer;
  }>();

  constructor() {}

  ngOnInit(): void {}

  ngOnChanges(): void {
    console.log('changed!');
  }

  increment() {
    const previousValue = +(this.question?.answer || 0);
    this.question.answer = (previousValue + 1).toString();
  }
  decrement() {
    const previousValue = +(this.question?.answer || 0);
    this.question.answer = (previousValue - 1).toString();
  }
}
