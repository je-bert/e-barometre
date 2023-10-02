import { Component, OnInit } from '@angular/core';
import { Observable, tap } from 'rxjs';
import { Invoice } from 'src/app/models/invoice';
import { InvoicesService } from 'src/app/services/invoices.service';

declare var Stripe: any;

@Component({
  selector: 'app-orders',
  templateUrl: './orders.component.html',
  styleUrls: ['./orders.component.scss'],
  providers: [InvoicesService],
})
export class OrdersComponent implements OnInit {
  public invoices$: Observable<Invoice[]> | undefined;
  public publishabeKey$: Observable<string> | undefined;
  public isAccordionOpen: { [key: number]: boolean } = {}; // Initialize accordion state

  constructor(private invoicesService: InvoicesService) {}

  public getInvoices(): void {
    this.invoices$ = this.invoicesService.getAllInvoices();
    this.invoices$.pipe(tap(console.log));
  }

  redirectToStripeCheckout(sessionId: string): void {
    this.invoicesService.getPublishableKey().subscribe((key: any) => {
      this.publishabeKey$ = key.publishableKey;
      const stripe = Stripe(
        'pk_test_51Nv4P9GGkVCNuBu2FPGlfjpam0fJGSHZM5B3fPYEjkAT7rN9LSgjGRvnEDUVb1q1JAOaqdoM9YtVnqiHNfAqqcgY00Wqjf8tHK'
      );
      stripe
        .redirectToCheckout({
          sessionId: sessionId,
        })
        .then((result: any) => {
          if (result.error) {
            console.error(result.error.message);
          }
        });
    });
  }

  public formatPrice(price: number): string {
    return '$' + (price / 100).toFixed(2);
  }

  public formatDate(date: string): string {
    const dateObj = new Date(date);
    return dateObj.toLocaleDateString('fr-CA', {
      year: 'numeric',
      month: 'short',
      day: 'numeric',
    });
  }

  public formatStatus(status: string): string {
    switch (status) {
      case 'paid':
        return 'Payé';
      case 'unpaid':
        return 'Non payé';
      case 'failed':
        return 'Échoué';
      case 'pending':
        return 'En attente';
      case 'expired':
        return 'Expiré';
      default:
        return status;
    }
  }

  public formatStatusColor(status: string): string {
    switch (status) {
      case 'paid':
        return 'green';
      case 'unpaid':
        return 'orange';
      case 'failed':
        return 'red';
      case 'pending':
        return 'yellow';
      default:
        return 'blue';
    }
  }

  // Function to toggle the accordion state
  public toggleAccordion(invoiceId: number): void {
    this.isAccordionOpen[invoiceId] = !this.isAccordionOpen[invoiceId];
  }

  ngOnInit(): void {
    this.getInvoices();
  }
}
