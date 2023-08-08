import { Component, OnInit } from '@angular/core';

import {
  NotificationService,
  NotificationData,
} from 'src/app/services/notification.service';

import { HttpClient } from '@angular/common/http';
import { Router } from '@angular/router';
import { environment } from 'src/environments/environment';

@Component({
  selector: 'app-tests',
  templateUrl: './tests.component.html',
  styleUrls: ['./tests.component.scss'],
})
export class TestsComponent implements OnInit {
  constructor(
    private notificationService: NotificationService,
    private http: HttpClient,
    private router: Router
  ) {}

  public testNotification(
    message: string,
    type: NotificationData['type']
  ): void {
    this.notificationService.show({
      message,
      type,
      duration: 20000,
    });
  }

  public getTeapot(): void {
    this.http.get(environment.apiUrl + '/teapot').subscribe({
      next: () => {},
      error: (error) => {
        console.log(error);
      },
    });
  }

  public getNotAuth(): void {
    this.http.get(environment.apiUrl + '/not-auth').subscribe({
      next: () => {},
      error: (err: { error: { message: string } }) => {
        console.log(err.error.message);
        window.sessionStorage.clear();
        this.router.navigateByUrl('/auth-wall');
      },
    });
  }

  public kaboom() {
    this.http.get<{ message: string }>(environment.apiUrl + '/boom').subscribe({
      next: (res) => {
        console.log(res);
      },
      error: (error) => {
        console.log(error);
      },
    });
  }

  public resetAnswers() {
    // TODO (Jeremie)
  }

  ngOnInit(): void {}
}
