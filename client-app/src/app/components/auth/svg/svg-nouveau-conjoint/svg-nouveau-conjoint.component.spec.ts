import { ComponentFixture, TestBed } from '@angular/core/testing';

import { SvgNouveauConjointComponent } from './svg-nouveau-conjoint.component';

describe('SvgNouveauConjointComponent', () => {
  let component: SvgNouveauConjointComponent;
  let fixture: ComponentFixture<SvgNouveauConjointComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ SvgNouveauConjointComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(SvgNouveauConjointComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
