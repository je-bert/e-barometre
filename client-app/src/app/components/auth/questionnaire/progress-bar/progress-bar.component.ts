import { Component, Input, OnInit } from '@angular/core';

@Component({
  selector: 'app-progress-bar[progress]',
  templateUrl: './progress-bar.component.html',
  styleUrls: ['./progress-bar.component.scss'],
})
export class ProgressBarComponent implements OnInit {
  @Input() progress!: string;

  constructor() {}

  ngOnInit(): void {}
}
