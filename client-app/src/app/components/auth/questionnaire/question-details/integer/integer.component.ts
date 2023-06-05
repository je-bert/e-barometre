import {
  Component,
  OnInit,
  Input,
  Output,
  EventEmitter,
  OnDestroy,
} from '@angular/core';
import { Subject } from 'rxjs';
import { takeUntil, debounceTime } from 'rxjs/operators';
import { ClientSideQuestion, QuestionAnswer } from 'src/app/models/question';

@Component({
  selector: 'app-integer',
  templateUrl: './integer.component.html',
  styleUrls: ['./integer.component.scss'],
})
export class IntegerComponent implements OnInit, OnDestroy {
  @Input() questionnaireColor!: string;

  @Input() question!: ClientSideQuestion;

  @Output() answerPicked = new EventEmitter<{
    question: ClientSideQuestion;
    answer: QuestionAnswer;
  }>();

  answerChanged$ = new Subject<void>();

  destroy$ = new Subject<void>();

  constructor() {}

  ngOnInit(): void {
    this.answerChanged$
      .pipe(takeUntil(this.destroy$), debounceTime(750))
      .subscribe(() => {
        console.log('answer changed!!!');

        const answer = this.question.answer;
        const question = this.question;

        this.answerPicked.emit({
          question,
          answer,
        });
      });
  }

  ngOnChanges(): void {
    console.log('changed!');
  }

  increment() {
    const previousValue = +(this.question?.answer || 0);
    this.question.answer = (previousValue + 1).toString();
    this.answerChanged$.next();
  }
  decrement() {
    const previousValue = +(this.question?.answer || 0);
    this.question.answer = (previousValue - 1).toString();
    this.answerChanged$.next();
  }

  ngOnDestroy() {
    this.destroy$.next();
    this.destroy$.complete();
  }
}
