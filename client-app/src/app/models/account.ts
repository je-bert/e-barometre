export interface Account {
  user_id: number;
  first_name: string;
  last_name: string;
  email: string;
  password: string; //TODO backend api for password not created? GET
  phone_number: number;
  date_logged_in: Date;
  date_created: Date;
  role: string;
}
