import { AfterViewInit, Component, Input, ElementRef, ViewChild, Output, EventEmitter } from '@angular/core';
import { Observable } from 'rxjs';

import autoAnimate from '@formkit/auto-animate';

@Component({
  selector: 'app-question-list',
  template: `

<div #questionListContainer>
    <ng-container *ngFor="let question of questions$ | async">
       <div 
       class="tw-my-12 tw-relative"
        [ngClass]="{ 'tw-opacity-50': answers[question.question_id] !== null }">
          <app-question  (questionAnswered)="questionAnswered.emit($event)" [question]='question'/>
       </div> 
    </ng-container>
</div>
  `,
  styles: [
  ]
})
export class QuestionListComponent implements AfterViewInit {


  @Input() questions$!: Observable<any[]>;
  @Input() answers!: Record<string, string | null>;

  @ViewChild('questionListContainer') containerRef!: ElementRef<HTMLDivElement>;


  @Output() questionAnswered = new EventEmitter<{ questionId: string; questionAnswer: string }>();

  ngAfterViewInit(): void {
    const container = this.containerRef.nativeElement;

    autoAnimate(container);
  }

}
