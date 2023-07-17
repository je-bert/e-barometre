import { Injectable } from '@angular/core';
import { MatSnackBar } from '@angular/material/snack-bar';
import { NotificationComponent } from '../components/shared/notification/notification.component';

export interface NotificationData {
  message: string;
  type: 'success' | 'danger' | 'warning' | 'info';
  duration?: number;
}

@Injectable({
  providedIn: 'root',
})
export class NotificationService {
  constructor(private snackBar: MatSnackBar) {}

  public show({ message, type, duration = 5000 }: NotificationData) {
    this.snackBar.openFromComponent(NotificationComponent, {
      duration: duration,
      data: {
        message,
        type,
      },
    });
  }

  public dismiss() {
    this.snackBar.dismiss();
  }
}
