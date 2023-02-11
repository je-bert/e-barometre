import {
  Component,
  OnInit,
  ViewChild,
  Input,
  ViewContainerRef,
} from '@angular/core';

@Component({
  selector: 'app-svg-enfant',
  templateUrl: './svg-enfant.component.html',
  styleUrls: ['./svg-enfant.component.scss'],
})
export class SvgEnfantComponent implements OnInit {
  @ViewChild('childTemplate', { static: true }) template: any;

  @Input() currentStep!: number;

  constructor(private viewContainerRef: ViewContainerRef) {}

  ngOnInit(): void {
    this.viewContainerRef.createEmbeddedView(this.template);
  }
}
