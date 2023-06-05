import { Component, Inject, OnInit } from '@angular/core';
import { MAT_SNACK_BAR_DATA } from '@angular/material/snack-bar';

import {
  NotificationData,
  NotificationService,
} from 'src/app/services/notification.service';

@Component({
  selector: 'app-notification',
  templateUrl: './notification.component.html',
  styleUrls: ['./notification.component.scss'],
})
export class NotificationComponent implements OnInit {
  public type: NotificationData['type'] = this.data.type;
  public message = this.data.message;

  constructor(
    @Inject(MAT_SNACK_BAR_DATA) public data: NotificationData,
    private notificationService: NotificationService
  ) {}

  public dismiss() {
    this.notificationService.dismiss();
  }

  ngOnInit(): void {}
}
