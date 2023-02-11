import {
  Component,
  EventEmitter,
  OnInit,
  Output,
  ViewChild,
} from '@angular/core';

import { ClrDatagridStateInterface } from '@clr/angular';

import { HttpClient } from '@angular/common/http';

import { MatExpansionPanel } from '@angular/material/expansion';
import { environment } from 'src/environments/environment';
import { map, tap } from 'rxjs';

type Survey = {
  color: string;
  cover_picture_url: string;
  description: string;
  index: number;
  name: string;
  status: string;
  survey_id: string;
  questionCount: number;
};

@Component({
  selector: 'app-admin-surveys-table',
  templateUrl: './admin-surveys-table.component.html',
  styleUrls: ['./admin-surveys-table.component.scss'],
})
export class AdminSurveysTableComponent implements OnInit {
  constructor(private http: HttpClient) {}

  @ViewChild('matExpansionPanel') matExpansionPanel!: MatExpansionPanel;
  @Output() onEditSurvey = new EventEmitter<string>();
  @Output() onViewQuestions = new EventEmitter<string>();
  @Output() onOpenPanel = new EventEmitter<void>();

  handleEditSurvey(surveyId: string) {
    this.onEditSurvey.emit(surveyId);
  }

  handleViewQuestions(surveyId: string) {
    if (this.matExpansionPanel) {
      this.matExpansionPanel.close();
    }
    this.onViewQuestions.emit(surveyId);
  }

  panelOpenState = false;

  handleOpenPanel() {
    this.panelOpenState = true;
    this.onOpenPanel.emit();
  }

  surveys: Survey[] = [];
  total = 0;
  loading = true;
  inventory = [];

  selectedSurvey: Survey | null = null;

  refresh(state: ClrDatagridStateInterface) {
    this.loading = true;
    // We convert the filters from an array to a map,
    // because that's what our backend-calling service is expecting
    let filters: { [prop: string]: any[] } = {};
    if (state.filters) {
      for (let filter of state.filters) {
        let { property, value } = <{ property: string; value: string }>filter;
        filters[property] = [value];
      }
    }

    this.http
      .get(environment.apiUrl + '/admin/surveys')
      .pipe(
        tap(console.log),
        map((data) => {
          return data.reduce((acc: any, value: any) => {
            if (value.survey_id === 'PCRA') {
              acc.push(value);
            }
            return acc;
          }, []);
        })
      )
      .subscribe((data: any) => {
        this.surveys = data;
        this.loading = false;
        this.total = data.length;
      });
  }

  onDelete(survey: Survey) {}

  ngOnInit(): void {
    // this.matExpansionPanel.open();
    // this.handleOpenPanel();
  }
}
