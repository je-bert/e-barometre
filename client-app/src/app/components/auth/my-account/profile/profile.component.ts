import { Component, OnInit } from '@angular/core';
import { Observable } from 'rxjs';
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
  public newPassword: Observable<string> | undefined; // Currently debating on using observables or passing the values as parameters using angular's property binding.
  public isDisabled: boolean = false;

  constructor(private accountService: AccountService, private router: Router) {}

  public toggleDelete(): void {
    this.isDisabled = !this.isDisabled;
  }

  // Call the service here.
  public deleteAccount() {
    this.accountService.deleteAccount().subscribe();
    window.sessionStorage.removeItem('token');
    this.router.navigateByUrl('/auth-wall');
  }
  public updateAccount() {}
  public updatePassword() {}

  ngOnInit(): void {
    this.accountService.getAccount().subscribe((account: Account) => {
      this.account = account;
    });
  }
}
