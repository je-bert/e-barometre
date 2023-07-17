import {
  Component,
  OnInit,
  ViewChild,
  Input,
  ViewContainerRef,
} from '@angular/core';

@Component({
  selector: 'app-svg-coparent',
  templateUrl: './svg-coparent.component.html',
  styleUrls: ['./svg-coparent.component.scss'],
})
export class SvgCoparentComponent implements OnInit {
  @ViewChild('childTemplate', { static: true }) template: any;

  @Input() currentStep!: number;

  constructor(private viewContainerRef: ViewContainerRef) {}

  ngOnInit(): void {
    this.viewContainerRef.createEmbeddedView(this.template);
  }
}
