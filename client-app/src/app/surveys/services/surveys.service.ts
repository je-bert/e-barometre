import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { map, tap } from 'rxjs/operators';

@Injectable({
  providedIn: 'root'
})
export class SurveysService {

  constructor(private http: HttpClient) { }


  getDemoQuestions() {
    return this.http.get<{ questions: { question_id: string }[] }>('http://localhost:3000/api/surveys/B').pipe(
      map(survey => survey.questions)
    )
  }


  demoSubmitAnswer(answers: Record<string, string | null>) {

    const answerList = Object.entries(answers)
      .filter(([_, value]) => value !== null)
      .map(([key, value]) => ({ question_id: key, value }))

    return this.http.put('http://localhost:3000/api/answers', { answers: answerList })

  }
}
