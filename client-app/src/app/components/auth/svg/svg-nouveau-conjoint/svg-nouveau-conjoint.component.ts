import {
  Component,
  Input,
  OnInit,
  ViewChild,
  ViewContainerRef,
} from '@angular/core';

@Component({
  selector: 'app-svg-nouveau-conjoint',
  templateUrl: './svg-nouveau-conjoint.component.html',
  styleUrls: ['./svg-nouveau-conjoint.component.scss'],
})
export class SvgNouveauConjointComponent implements OnInit {
  @ViewChild('childTemplate', { static: true }) template: any;

  @Input() currentStep!: number;

  constructor(private viewContainerRef: ViewContainerRef) {}

  ngOnInit(): void {
    this.viewContainerRef.createEmbeddedView(this.template);
  }
}
