import { ComponentFixture, TestBed } from '@angular/core/testing';

import { SvgParentRepondantComponent } from './svg-parent-repondant.component';

describe('SvgParentRepondantComponent', () => {
  let component: SvgParentRepondantComponent;
  let fixture: ComponentFixture<SvgParentRepondantComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ SvgParentRepondantComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(SvgParentRepondantComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
