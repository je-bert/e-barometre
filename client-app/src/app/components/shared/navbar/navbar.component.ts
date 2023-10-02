import { Component, OnInit } from '@angular/core';
import { AccountService } from 'src/app/services/account.service';
import { Account } from 'src/app/models/account';
@Component({
  selector: 'app-navbar',
  templateUrl: './navbar.component.html',
  styleUrls: ['./navbar.component.scss'],
  providers: [AccountService],
})
export class NavbarComponent implements OnInit {
  public accountFirstName: String | undefined;
  public hasUnpaidInvoice: boolean = false;

  constructor(private accountService: AccountService) {}

  ngOnInit(): void {
    this.accountService.getAccount().subscribe((account: Account) => {
      this.accountFirstName = account.first_name;
      this.hasUnpaidInvoice = account.has_unpaid_invoice;
    });
  }
}
