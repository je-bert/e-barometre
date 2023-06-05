import { ComponentFixture, TestBed } from '@angular/core/testing';

import { AdminSurveyTableComponent } from './admin-survey-table.component';

describe('AdminSurveyTableComponent', () => {
  let component: AdminSurveyTableComponent;
  let fixture: ComponentFixture<AdminSurveyTableComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ AdminSurveyTableComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(AdminSurveyTableComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
