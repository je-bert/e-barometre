import { Component, OnInit, ViewChild } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { AuthService } from 'src/app/services/auth.service';
import { NotificationService } from 'src/app/services/notification.service';
import { FormControl, FormGroup, Validators, ValidatorFn, AbstractControl } from '@angular/forms';

@Component({
  selector: 'app-change-password',
  templateUrl: './change-password.component.html',
  styleUrls: ['./change-password.component.scss']
})
export class ChangePasswordComponent implements OnInit {
  public token: string;
  public id: number;
  public showPassword = false;
  public changePasswordForm = new FormGroup({
    password1: new FormControl('', [Validators.required]),
    password2: new FormControl('', [Validators.required]),
  }, { validators: passwordMatchValidator });

  constructor(
    private authService: AuthService,
    private notificationService: NotificationService,
    private route: ActivatedRoute,
    private router: Router
    ) { }

  ngOnInit(): void {
    this.route.queryParams.subscribe(params => {
      this.token = params['token'];
      this.id = +params['id'] ?? 0;
    });
  }

  public onPasswordToggleChange(event: Event) {
    const checked = (event.target as HTMLInputElement).checked;
    this.showPassword = checked;
  }

  public async onChangePasswordSubmit() {
    const { password1, password2 } = this.changePasswordForm.value;

    if (this.changePasswordForm.invalid) {
      if (this.changePasswordForm.hasError('passwordMismatch')) {
        this.notificationService.show({
          message: 'Les mots de passe ne correspondent pas',
          type: 'warning',
        });
        return;
      }
      this.notificationService.show({
        message: 'Veuillez remplir tous les champs',
        type: 'warning',
      });
      return;
    }

    try {
      await this.authService.postCompleteResetPassword(this.token, this.id, password1 ?? '');
      this.router.navigateByUrl('/login');
      this.notificationService.show({
        message: 'Votre mot de passe a bien été modifié',
        type: 'success',
      });
    } catch (error: any) {
      console.error(error);
      this.notificationService.show({
        message: error.error,
        type: 'warning',
      });
    }
  }
}

const passwordMatchValidator: ValidatorFn = (control: AbstractControl): {[key: string]: any} | null => {
  const password1 = control.get('password1');
  const password2 = control.get('password2');

  const errors = password1 && password2 && password1.value !== password2.value ? { 'passwordMismatch': true } : null;
  return errors;
};
