import { ComponentFixture, TestBed } from '@angular/core/testing';

import { LabeledLadderComponent } from './labeled-ladder.component';

describe('LabeledLadderComponent', () => {
  let component: LabeledLadderComponent;
  let fixture: ComponentFixture<LabeledLadderComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ LabeledLadderComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(LabeledLadderComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
