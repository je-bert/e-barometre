import { Component, OnInit } from '@angular/core';
import { Observable, tap } from 'rxjs';
import { Invoice } from 'src/app/models/invoice';
import { InvoicesService } from 'src/app/services/invoices.service';

@Component({
  selector: 'app-orders',
  templateUrl: './orders.component.html',
  styleUrls: ['./orders.component.scss'],
  providers: [InvoicesService],
})
export class OrdersComponent implements OnInit {
  public invoices$: Observable<Invoice[]> | undefined;
  public isAccordionOpen: { [key: number]: boolean } = {}; // Initialize accordion state

  constructor(private invoicesService: InvoicesService) {}

  public getInvoices(): void {
    this.invoices$ = this.invoicesService.getAllInvoices();
    this.invoices$.pipe(tap(console.log));
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
