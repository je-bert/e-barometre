import { Component } from '@angular/core';
import { AuthService } from 'src/app/services/auth.service';
import { NotificationService } from 'src/app/services/notification.service';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.scss'],
})
export class LoginComponent {
  public email = '';
  public password = '';
  public showPassword = false;
  public conditions = true;

  constructor(
    private authService: AuthService,
    private notificationService: NotificationService
  ) {}

  public onPasswordToggleChange(event: Event) {
    const checked = (event.target as HTMLInputElement).checked;
    this.showPassword = checked;
  }

  public onAcceptConditions() {
    this.conditions = true;
  }

  async login() {
    if (!this.conditions) {
      this.notificationService.show({
        message: 'You must accept the terms and conditions',
        type: 'warning',
      });
      return;
    }
    await this.authService.login(this.email, this.password, this.conditions);
  }
}
