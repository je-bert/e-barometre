import { ComponentFixture, TestBed } from '@angular/core/testing';

import { AuthWallComponent } from './auth-wall.component';

describe('AuthWallComponent', () => {
  let component: AuthWallComponent;
  let fixture: ComponentFixture<AuthWallComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ AuthWallComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(AuthWallComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
