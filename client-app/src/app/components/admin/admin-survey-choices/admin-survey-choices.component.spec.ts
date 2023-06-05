import { ComponentFixture, TestBed } from '@angular/core/testing';

import { AdminSurveyChoicesComponent } from './admin-survey-choices.component';

describe('AdminSurveyChoicesComponent', () => {
  let component: AdminSurveyChoicesComponent;
  let fixture: ComponentFixture<AdminSurveyChoicesComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ AdminSurveyChoicesComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(AdminSurveyChoicesComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
