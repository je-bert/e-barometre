import { Component, Input, OnInit } from '@angular/core';

@Component({
  selector: 'app-progress-bar[progress]',
  templateUrl: './progress-bar.component.html',
  styleUrls: ['./progress-bar.component.scss'],
})
export class ProgressBarComponent implements OnInit {
  @Input() progress!: string;
  @Input() bgColor: string | null = null;
  @Input() barColor = '#102485';
  @Input() title = 'Parent répondant';

  constructor() {}

  ngOnInit(): void {}
}
