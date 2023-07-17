import { ComponentFixture, TestBed } from '@angular/core/testing';

import { FinalReportsComponent } from './final-reports.component';

describe('FinalReportsComponent', () => {
  let component: FinalReportsComponent;
  let fixture: ComponentFixture<FinalReportsComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ FinalReportsComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(FinalReportsComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
