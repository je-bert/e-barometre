import { Component } from '@angular/core';
import { Router } from '@angular/router';
import { AccountService } from 'src/app/services/account.service';
import { Account } from 'src/app/models/account';

@Component({
  selector: 'app-my-account',
  templateUrl: './my-account.component.html',
  styleUrls: ['./my-account.component.scss'],
  providers: [AccountService],
})
export class MyAccountComponent {
  constructor(private router: Router, private accountService: AccountService) {}

  public accountFullName: string | undefined;
  public hasUnpaidInvoice: boolean = false;

  logout() {
    window.sessionStorage.removeItem('token');
    this.router.navigateByUrl('/auth-wall');
  }
  ngOnInit(): void {
    this.accountService.getAccount().subscribe((account: Account) => {
      this.accountFullName = account.first_name + ' ' + account.last_name;
      this.hasUnpaidInvoice = account.has_unpaid_invoice;
    });
  }
}
