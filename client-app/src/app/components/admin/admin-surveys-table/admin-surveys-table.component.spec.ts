import { ComponentFixture, TestBed } from '@angular/core/testing';

import { AdminSurveysTableComponent } from './admin-surveys-table.component';

describe('AdminSurveysTableComponent', () => {
  let component: AdminSurveysTableComponent;
  let fixture: ComponentFixture<AdminSurveysTableComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ AdminSurveysTableComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(AdminSurveysTableComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
