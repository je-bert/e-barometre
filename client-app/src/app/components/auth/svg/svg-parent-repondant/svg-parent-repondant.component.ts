import {
  Component,
  Input,
  OnInit,
  ViewChild,
  ViewContainerRef,
} from '@angular/core';

@Component({
  selector: 'app-svg-parent-repondant',
  templateUrl: './svg-parent-repondant.component.html',
  styleUrls: ['./svg-parent-repondant.component.scss'],
})
export class SvgParentRepondantComponent implements OnInit {
  @ViewChild('childTemplate', { static: true }) template: any;

  @Input() currentStep!: number;

  constructor(private viewContainerRef: ViewContainerRef) {}

  ngOnInit(): void {
    this.viewContainerRef.createEmbeddedView(this.template);
  }
}
