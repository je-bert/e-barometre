import { Component, OnInit } from '@angular/core';
import { Observable } from 'rxjs';
import { Account } from 'src/app/models/account';
import { AccountService } from 'src/app/services/account.service';
import { FinalReportService } from 'src/app/services/final_reports.service';

declare var Stripe: any;
@Component({
  selector: 'app-final-reports',
  templateUrl: './final-reports.component.html',
  styleUrls: ['./final-reports.component.scss'],
  providers: [FinalReportService, AccountService],
})
export class FinalReportsComponent implements OnInit {
  constructor(
    private finalReportService: FinalReportService,
    private accountService: AccountService
  ) {}

  public publishableKey: String | undefined;
  public userEmail: String;
  private sessionId: String | undefined;

  public redirectStripeCheckout(reportType: String): void {
    this.finalReportService.getPublishableKey().subscribe((key) => {
      this.publishableKey = key.publishable_key;
      const stripe = Stripe(this.publishableKey);
      this.finalReportService
        .getSessionId(reportType, this.userEmail)
        .subscribe((sessionId) => {
          this.sessionId = sessionId.session_id;
          console.log(this.sessionId);
        });
      return stripe.redirectToCheckout({ sessionId: this.sessionId });
    });
  }

  ngOnInit(): void {
    this.accountService.getAccount().subscribe((account: Account) => {
      this.userEmail = account.email;
    });
  }
}
