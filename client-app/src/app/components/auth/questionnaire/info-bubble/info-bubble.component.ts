import { Component, Input, OnInit } from '@angular/core';

import { ClientSideQuestion } from 'src/app/models/question';

@Component({
  selector: 'app-info-bubble[question]',
  templateUrl: './info-bubble.component.html',
  styleUrls: ['./info-bubble.component.scss'],
})
export class InfoBubbleComponent implements OnInit {
  @Input() question!: ClientSideQuestion;

  public opacity = 0;

  constructor() {}

  breakLines(text: string): string {
    return text.replace(/\\n|\/n/g, '<br>');
  }

  ngOnInit(): void {
    setTimeout(() => {
      this.opacity = 1;
    });
  }
}
