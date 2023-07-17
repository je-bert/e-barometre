import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';

import { NotificationService } from 'src/app/services/notification.service';

@Component({
  selector: 'app-admin-login',
  templateUrl: './admin-login.component.html',
  styleUrls: ['./admin-login.component.scss'],
})
export class AdminLoginComponent implements OnInit {
  public username = '';
  public password = '';

  constructor(
    private router: Router,

    private notificationService: NotificationService
  ) {}

  login() {
    if (this.username === 'admin' && this.password === 'root') {
      window.sessionStorage.setItem('isAdmin', 'true');
      this.router.navigateByUrl('/admin/admin-panel');
    } else {
      this.notificationService.show({
        message: 'Identifiants invalides',
        type: 'warning',
      });
    }
  }

  ngOnInit(): void {}
}
