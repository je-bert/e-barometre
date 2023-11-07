import { Component, Input } from '@angular/core';

@Component({
  selector: 'app-page-header[title]',
  templateUrl: './page-header.component.html',
  styleUrls: ['./page-header.component.scss'],
})
export class PageHeaderComponent {
  @Input() title!: string;

  @Input() questionnaireColor?: string;

  ngOnInit() {}
}
