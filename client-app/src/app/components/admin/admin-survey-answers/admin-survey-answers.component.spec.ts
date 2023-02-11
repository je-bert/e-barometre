import { ComponentFixture, TestBed } from '@angular/core/testing';

import { AdminSurveyAnswersComponent } from './admin-survey-answers.component';

describe('AdminSurveyAnswersComponent', () => {
  let component: AdminSurveyAnswersComponent;
  let fixture: ComponentFixture<AdminSurveyAnswersComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ AdminSurveyAnswersComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(AdminSurveyAnswersComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
