import { ComponentFixture, TestBed } from '@angular/core/testing';

import { SvgEnfantComponent } from './svg-enfant.component';

describe('SvgEnfantComponent', () => {
  let component: SvgEnfantComponent;
  let fixture: ComponentFixture<SvgEnfantComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ SvgEnfantComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(SvgEnfantComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
