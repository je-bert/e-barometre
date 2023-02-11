import { Question } from './question';

export interface Questionnaire {
  survey_id: string;
  name: string;
  description: string;
  color: string;
  cover_picture_url: string;
  is_available: boolean;
  is_completed: boolean;

  questions: Question[];
}
