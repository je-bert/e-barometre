import { ComponentFixture, TestBed } from '@angular/core/testing';

import { AvailableQuestionnairesComponent } from './available-questionnaires.component';

describe('AvailableQuestionnairesComponent', () => {
  let component: AvailableQuestionnairesComponent;
  let fixture: ComponentFixture<AvailableQuestionnairesComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ AvailableQuestionnairesComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(AvailableQuestionnairesComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
