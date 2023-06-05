import { HttpClient } from '@angular/common/http';
import { Component } from '@angular/core';
import { FormBuilder, FormArray } from '@angular/forms';
import { tap, timer } from 'rxjs';
import { environment } from 'src/environments/environment';

@Component({
  selector: 'app-admin-survey-choices',
  templateUrl: './admin-survey-choices.component.html',
  styleUrls: ['./admin-survey-choices.component.scss'],
})
export class AdminSurveyChoicesComponent {
  labels$ = this.http
    .get<SurveyLabel[]>(`${environment.apiUrl}/admin/survey-labels`)
    .pipe(
      tap((labels) => {
        labels.forEach((label) => {
          const name = label.name;

          (this.labelsForm.get('labels') as FormArray).push(
            this.fb.group({
              name: [name],
              values: this.fb.array([
                ...label.values.map((value) =>
                  this.fb.group({ value: [value.value], label: [value.label] })
                ),
              ]),
            })
          );
        });
      })
    );

  labelsForm = this.fb.group({
    labels: this.fb.array([]),
  });

  getLabels = () => {
    return (this.labelsForm.get('labels') as FormArray).controls;
  };

  getValues = (labelIndex: number) => {
    return (
      (this.labelsForm.get('labels') as FormArray)
        .at(labelIndex)
        .get('values') as FormArray
    ).controls;
  };

  constructor(private http: HttpClient, private fb: FormBuilder) {}

  ngAfterViewInit() {
    this.labelsForm.valueChanges.pipe().subscribe();

    if (window.location.hash) {
      timer(500).subscribe(() => {
        const scrollTarget = document.querySelector(window.location.hash);

        if (scrollTarget === null) return;

        scrollTarget.scrollIntoView({ behavior: 'smooth' });
      });
    }
  }
}

type SurveyLabel = {
  name: string;
  values: {
    value: number | null;
    label: string;
  }[];
};
