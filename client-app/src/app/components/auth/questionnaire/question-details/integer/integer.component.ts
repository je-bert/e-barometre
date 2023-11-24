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

  answerChanged$ = new Subject<number>();

  destroy$ = new Subject<void>();
  value = 0;

  constructor() {}

  ngOnInit(): void {
    this.value =
      this.question.answer === '-1'
        ? this.question.min_value || 0
        : +(this.question.answer || 0);
    this.answerChanged$
      .pipe(takeUntil(this.destroy$), debounceTime(750))
      .subscribe((answer) => {
        console.log('answer changed!!!');
        answer = Math.max(answer, this.question.min_value || 0);
        answer = Math.min(answer, this.question.max_value || 0);

        this.question.answer = answer.toString();
        const question = this.question;

        this.answerPicked.emit({
          question,
          answer: answer.toString(),
        });
      });
  }

  ngOnChanges(): void {
    console.log('changed!');
  }

  increment() {
    this.value = Math.min(
      this.value + 1,
      this.question.max_value || Number.MAX_SAFE_INTEGER
    );
    this.answerChanged$.next(this.value);
  }
  decrement() {
    this.value = Math.max(
      this.value - 1,
      this.question.min_value || Number.MIN_SAFE_INTEGER
    );
    this.answerChanged$.next(this.value);
  }

  ngOnDestroy() {
    this.destroy$.next();
    this.destroy$.complete();
  }
}
