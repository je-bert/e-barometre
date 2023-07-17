import { ComponentFixture, TestBed } from '@angular/core/testing';

import { CannotSkipLastWarningComponent } from './cannot-skip-last-warning.component';

describe('CannotSkipLastWarningComponent', () => {
  let component: CannotSkipLastWarningComponent;
  let fixture: ComponentFixture<CannotSkipLastWarningComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ CannotSkipLastWarningComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(CannotSkipLastWarningComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
