import {
  Component,
  Input,
  OnInit,
  Output,
  EventEmitter,
  ViewChild,
  ElementRef,
} from '@angular/core';

import {
  ClientSideQuestion,
  QuestionAnswer,
} from '../../../../models/question';

import autoAnimate from '@formkit/auto-animate';

@Component({
  selector: 'app-questions-list',
  templateUrl: './questions-list.component.html',
  styleUrls: ['./questions-list.component.scss'],
})
export class QuestionsListComponent implements OnInit {
  @ViewChild('questionListContainer') containerRef!: ElementRef<HTMLDivElement>;

  @Input() questions: ClientSideQuestion[] = [];

  @Output() infoBubbleToggler = new EventEmitter<ClientSideQuestion>();
  onInfoBubbleOpen(question: ClientSideQuestion): void {
    this.infoBubbleToggler.emit(question);
  }

  @Output() answerPicker = new EventEmitter<{
    question: ClientSideQuestion;
    answer: QuestionAnswer;
  }>();

  @Output() questionSkipper = new EventEmitter<ClientSideQuestion>();

  @Output() confirmToggler = new EventEmitter<ClientSideQuestion>();

  onAnswer({
    question,
    answer,
  }: {
    question: ClientSideQuestion;
    answer: QuestionAnswer;
  }): void {
    this.answerPicker.emit({ question, answer });
  }

  onSkipForNow(question: ClientSideQuestion): void {
    this.questionSkipper.emit(question);
  }

  onConfirm(question: ClientSideQuestion): void {
    this.confirmToggler.emit(question);
  }

  constructor() {}

  ngOnInit(): void {}

  ngAfterViewInit(): void {
    const container = this.containerRef.nativeElement;

    autoAnimate(container);
  }
}
