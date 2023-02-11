import { ComponentFixture, TestBed } from '@angular/core/testing';

import { NumericLadderComponent } from './numeric-ladder.component';

describe('NumericLadderComponent', () => {
  let component: NumericLadderComponent;
  let fixture: ComponentFixture<NumericLadderComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ NumericLadderComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(NumericLadderComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
