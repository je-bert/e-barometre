import { ComponentFixture, TestBed } from '@angular/core/testing';

import { AdminGlossaryComponent } from './admin-glossary.component';

describe('AdminGlossaryComponent', () => {
  let component: AdminGlossaryComponent;
  let fixture: ComponentFixture<AdminGlossaryComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ AdminGlossaryComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(AdminGlossaryComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
