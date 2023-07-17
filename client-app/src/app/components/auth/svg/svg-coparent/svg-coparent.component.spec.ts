import { ComponentFixture, TestBed } from '@angular/core/testing';

import { SvgCoparentComponent } from './svg-coparent.component';

describe('SvgCoparentComponent', () => {
  let component: SvgCoparentComponent;
  let fixture: ComponentFixture<SvgCoparentComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ SvgCoparentComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(SvgCoparentComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
