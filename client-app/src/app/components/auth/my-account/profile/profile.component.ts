import { Component, Input, OnInit } from '@angular/core';
import { Account } from 'src/app/models/account';
import { AccountService } from 'src/app/services/account.service';
import { Router } from '@angular/router';
import { ErrorResponse, SuccessResponse } from 'src/app/models/response';
import { NotificationService } from 'src/app/services/notification.service';

@Component({
  selector: 'app-profile',
  templateUrl: './profile.component.html',
  styleUrls: ['./profile.component.scss'],
  providers: [AccountService],
})
export class ProfileComponent implements OnInit {
  public account: Account | undefined;

  @Input() currentPassword: String = '';
  @Input() newPassword: String = '';
  @Input() confirmationPassword: String = '';
  @Input() firstName: String | undefined;
  @Input() lastName: String | undefined;
  @Input() email: String | undefined;

  public isDisabled: boolean = true;
  public responseMessage: String = '';
  public isAccountUpdated: boolean = false;

  constructor(
    private accountService: AccountService,
    private router: Router,
    private notificationService: NotificationService
  ) {}

  public toggleDelete(): void {
    this.isDisabled = !this.isDisabled;
  }

  public undoAccountChange(): void {
    this.firstName = this.account?.first_name;
    this.lastName = this.account?.last_name;
    this.email = this.account?.email;
  }

  public undoPasswordChange(): void {
    this.currentPassword = '';
    this.newPassword = '';
    this.confirmationPassword = '';
  }

  // Call the service here.
  public deleteAccount() {
    this.accountService.deleteAccount().subscribe({
      next: () => {
        window.sessionStorage.removeItem('token');
        this.router.navigateByUrl('/auth-wall');
      },
      error: (response: ErrorResponse) => {
        this.responseMessage = response.error.message;
        this.notificationService.show({
          message: `${this.responseMessage}`,
          type: 'danger',
        });
      },
    });
  }

  public updateAccount() {
    this.accountService
      .updateAccount(this.firstName, this.lastName, this.email)
      .subscribe({
        next: () => {
          window.location.reload();
        },
        error: (response: ErrorResponse) => {
          this.responseMessage = response.error.message;
          this.notificationService.show({
            message: `${this.responseMessage}`,
            type: 'danger',
          });
        },
      });
  }

  public updatePassword() {
    if (this.newPassword !== this.confirmationPassword) {
      this.notificationService.show({
        message:
          'Le nouveau mot de passe et la confirmation du nouveau mot de passe ne correspondent pas',
        type: 'danger',
      });
      return;
    }

    this.accountService
      .setPassword(this.currentPassword, this.newPassword)
      .subscribe({
        next: (response: SuccessResponse) => {
          this.responseMessage = response.body.message;
          this.notificationService.show({
            message: `${this.responseMessage}`,
            type: 'success',
          });
        },
        error: (response: ErrorResponse) => {
          this.responseMessage = response.error.message;
          this.notificationService.show({
            message: `${this.responseMessage}`,
            type: 'danger',
          });
        },
      });
  }

  ngOnInit(): void {
    this.accountService.getAccount().subscribe((account: Account) => {
      this.account = account;
      this.firstName = account.first_name;
      this.lastName = account.last_name;
      this.email = account.email;
    });
  }
}
