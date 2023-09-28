export interface Invoice {
  invoice_id: number;
  amount_discount: number;
  amount_subtotal: number;
  amont_tax: number;
  amount_total: number;
  date_created: string;
  date_expiration: string;
  session_id: string;
  price_id: string;
  status: string;
  user_id: number;
  description: string;
}
