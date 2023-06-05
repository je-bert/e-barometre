import { Component, OnInit } from '@angular/core';
import { environment } from 'src/environments/environment';
import { HttpClient } from '@angular/common/http';
import { MatDialog } from '@angular/material/dialog';
import { DialogComponent } from '../shared/dialog/dialog.component';
import { NotificationService } from 'src/app/services/notification.service';

@Component({
  selector: 'app-admin',
  templateUrl: './admin.component.html',
  styleUrls: ['./admin.component.scss'],
})
export class AdminComponent implements OnInit {
  constructor(
    private http: HttpClient,
    public dialog: MatDialog,
    private notificationService: NotificationService
  ) {}

  resetSuccess = false;

  getIsAuth() {
    return window.sessionStorage.getItem('isAdmin');
  }

  openDialog(): void {
    const dialogRef = this.dialog.open(DialogComponent, {
      width: '250px',
      data: {
        title: 'Are you sure?',
        description: 'This will reset the database to its original state.',
      },
    });

    dialogRef.afterClosed().subscribe((result) => {
      if (result === 'Ok') {
        this.handleResetDB();
      }
    });
  }

  ngOnInit(): void {}

  handleResetDB() {
    this.http.get(environment.apiUrl + '/admin/reset').subscribe(() => {
      this.notificationService.show({
        message: 'Database reset successfully',
        type: 'success',
      });
    });
  }
}
