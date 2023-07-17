import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-cannot-skip-last-warning',
  templateUrl: './cannot-skip-last-warning.component.html',
  styleUrls: ['./cannot-skip-last-warning.component.scss'],
})
export class CannotSkipLastWarningComponent implements OnInit {
  public opacity = 0;

  ngOnInit(): void {
    setTimeout(() => {
      this.opacity = 1;
    });
  }
}
