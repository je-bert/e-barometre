import {
  Component,
  Input,
  Output,
  EventEmitter,
  ElementRef,
  ChangeDetectorRef,
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
  chosenSO: string | null = null;

  constructor(private elRef: ElementRef, private cdr: ChangeDetectorRef) {
    this.self = elRef.nativeElement as HTMLElement;

    this.self.addEventListener('click', (event) => {
      if (this.question.answer === '-1') {
        this.chosenSO = '-1';
      } else {
        this.chosenSO = null;
      }
      this.cdr.detectChanges();
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

  ngOnInit(): void {
    if (this.question.answer === '-1') {
      this.chosenSO = '-1';
    } else {
      this.chosenSO = null;
    }
  }
}
