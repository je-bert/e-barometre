import { Component } from '@angular/core';
import { Router, NavigationEnd, RouterEvent } from '@angular/router';
import { filter } from 'rxjs/operators';

@Component({
  selector: 'app-auth-wall',
  templateUrl: './auth-wall.component.html',
  styleUrls: ['./auth-wall.component.scss']
})
export class AuthWallComponent {
  public currentUrl: string = '';

  constructor(private router: Router) {
    this.router.events
      .pipe(filter((event: RouterEvent | any) => event instanceof NavigationEnd))
      .subscribe((event: NavigationEnd) => {
        this.currentUrl = event.url;
      });
  }

  public isBackButtonVisible(): boolean {
    return this.currentUrl.startsWith('/auth-wall/');
  }
}