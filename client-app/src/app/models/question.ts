export type Question =
  | SelectMultipleChoiceQuestion
  | SelectSingleChoiceQuestion
  | NumericLadderQuestion
  | LabeledLadderQuestion
  | YesNoQuestion
  | IntegerQuestion;

export interface ClientSideQuestion extends BaseQuestion {
  shouldBeDisplayed: boolean;
  isInfoBubbleOpen: boolean;
  hasOtherValueToSpecify: boolean;
  otherValue: string;
  isConfirmed: boolean;
  index: number;
}

interface BaseQuestion {
  survey_id: string;
  question_id: string;
  title: string;
  intro: string | null;
  type: QuestionType;
  answer: QuestionAnswer;
  condition: string | null; // condition -> seulement pour questionnaire actuel pour que client puisse dynamiquement afficher ou cacher la question basé sur les réponses
  choices?: QuestionChoice[];
  info_bubble_text: string | null;
  max_value?: number;
  min_value?: number;
}

type QuestionChoice = {
  label: string;
  value: string | null;
};

export type QuestionAnswer = string | null;

export type SaveQuestionAnswer = {
  question_id: string;
  value: string;
  custom_answer?: string;
};

type QuestionType =
  | 'select-single'
  | 'select-multiple'
  | 'numeric-ladder'
  | 'labeled-ladder'
  | 'binary'
  | 'integer';

interface SelectSingleChoiceQuestion extends BaseQuestion {
  type: 'select-single';
  choices: QuestionChoice[];
}

interface SelectMultipleChoiceQuestion extends BaseQuestion {
  type: 'select-multiple';
  choices: QuestionChoice[];
}

interface NumericLadderQuestion extends BaseQuestion {
  type: 'numeric-ladder';
}

interface LabeledLadderQuestion extends BaseQuestion {
  type: 'labeled-ladder';
  choices: QuestionChoice[];
}

interface YesNoQuestion extends BaseQuestion {
  type: 'binary';
}

export interface IntegerQuestion extends BaseQuestion {
  type: 'integer';
  max_value: number;
  min_value: number;
}
