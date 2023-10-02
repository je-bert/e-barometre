import { Component } from '@angular/core';
import { AuthService } from 'src/app/services/auth.service';
import { NotificationService } from 'src/app/services/notification.service';

@Component({
  selector: 'app-forgot-password',
  templateUrl: './forgot-password.component.html',
  styleUrls: ['./forgot-password.component.scss']
})
export class ForgotPasswordComponent {
  public isForgotPasswordSent = false;
  public email = '';

  constructor(private authService: AuthService, private notificationService: NotificationService) { }

  public async onForgotSubmit() {
    try {
      await this.authService.postResetPassword(this.email);
      this.isForgotPasswordSent = true;
    } catch (error: any) {
      console.error(error);
      this.notificationService.show({
        message: error.error,
        type: 'warning',
      });
    }
  }
}
