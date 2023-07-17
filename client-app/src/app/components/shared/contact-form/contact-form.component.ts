import { Component, ViewChild } from '@angular/core';
import { NgForm, NgModel } from '@angular/forms';

@Component({
  selector: 'app-contact-form',
  templateUrl: './contact-form.component.html',
  styleUrls: ['./contact-form.component.scss'],
})
export class ContactFormComponent {
  @ViewChild('contactForm') contactForm!: NgForm;

  public submitted = false;

  constructor() {}

  public fullName = '';
  public email = '';
  public phone = '';
  public howDidYouHear = '';
  public subject = '';
  public message = '';

  onSubmit(): void {
    if (this.contactForm.invalid) return;
    this.submitted = true;
    alert('TODO submit');
  }

  onReset(): void {
    // this.contactForm.reset();
  }
}
