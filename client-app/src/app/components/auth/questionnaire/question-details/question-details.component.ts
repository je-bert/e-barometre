import {
  Component,
  Input,
  Output,
  EventEmitter,
  ElementRef,
} from '@angular/core';
import { timer } from 'rxjs';

import {
  ClientSideQuestion,
  QuestionAnswer,
} from '../../../../models/question';

@Component({
  selector: 'app-question-details[question]',
  templateUrl: './question-details.component.html',
  styleUrls: ['./question-details.component.scss'],
})
export class QuestionDetailsComponent {
  @Input() question!: ClientSideQuestion;

  @Output() infoBubbleToggled = new EventEmitter<ClientSideQuestion>();
  @Output() confirmToggled = new EventEmitter<ClientSideQuestion>();

  @Output() answerPicked = new EventEmitter<{
    question: ClientSideQuestion;
    answer: QuestionAnswer;
  }>();

  @Output() skipForNow = new EventEmitter<ClientSideQuestion>();

  self: HTMLElement | null = null;

  constructor(private elRef: ElementRef) {
    this.self = elRef.nativeElement as HTMLElement;

    this.self.addEventListener('click', (event) => {
      if (!this.question.isConfirmed) return;

      timer(150).subscribe(() => {
        this.self?.parentElement?.nextElementSibling?.firstElementChild?.scrollIntoView(
          {
            behavior: 'smooth',
            block: 'center',
          }
        );
      });
    });
  }
}
