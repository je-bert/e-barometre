import { Component, Input, OnInit } from '@angular/core';
import { Account } from 'src/app/models/account';
import { AccountService } from 'src/app/services/account.service';
import { Router } from '@angular/router';

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
  public errorMessage: String = '';
  public isAccountUpdated: boolean = false;

  constructor(private accountService: AccountService, private router: Router) {}

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
    this.accountService
      .deleteAccount()
      .subscribe((status) => console.log(status));
    window.sessionStorage.removeItem('token');
    this.router.navigateByUrl('/auth-wall');
  }

  public updateAccount() {
    this.accountService
      .updateAccount(this.firstName, this.lastName, this.email)
      .subscribe({
        next: (response) => {
          window.location.reload();
        },
        error: (error) => {
          window.location.reload();
        },
      });
  }

  public updatePassword() {
    if (this.newPassword !== this.confirmationPassword) {
      this.errorMessage =
        'Le nouveau mot de passe et la confirmation du nouveau mot de passe ne correspondent pas';
      return;
    }

    this.accountService
      .setPassword(this.currentPassword, this.newPassword)
      .subscribe((response) => console.log(response));
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
