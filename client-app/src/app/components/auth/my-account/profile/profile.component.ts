import { Component, OnInit } from '@angular/core';
import { Observable } from 'rxjs';
import { Account } from 'src/app/models/account';
import { AccountService } from 'src/app/services/account.service';

@Component({
  selector: 'app-profile',
  templateUrl: './profile.component.html',
  styleUrls: ['./profile.component.scss'],
  providers: [AccountService],
})
export class ProfileComponent implements OnInit {
  public account: Account | undefined;
  public newPassword: Observable<string> | undefined; // Currently debating on using observables or passing the values as parameters using angular's property binding.

  constructor(private accountService: AccountService) {}

  //Call the service here.
  public deleteAccount() {}
  public updateAccount() {}
  public updatePassword() {}

  ngOnInit(): void {
    this.accountService.getAccount().subscribe((account: Account) => {
      this.account = account;
    });
    console.log(this.account?.password);
  }
}
