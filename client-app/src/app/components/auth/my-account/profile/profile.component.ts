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
  public isDisabled: boolean = true;

  constructor(private accountService: AccountService, private router: Router) {}

  public toggleDelete(): void {
    this.isDisabled = !this.isDisabled;
  }

  // Call the service here.
  public deleteAccount() {
    this.accountService
      .deleteAccount()
      .subscribe((status) => console.log(status));
    // window.sessionStorage.removeItem('token');
    // this.router.navigateByUrl('/auth-wall');
  }
  public updateAccount() {}

  public updatePassword() {
    if (this.newPassword !== this.confirmationPassword) {
      alert('Please put the same password');
      return;
    }

    this.accountService
      .setPassword(this.currentPassword, this.newPassword)
      .subscribe((status) => console.log(status));
  }

  ngOnInit(): void {
    this.accountService.getAccount().subscribe((account: Account) => {
      this.account = account;
    });
  }
}
