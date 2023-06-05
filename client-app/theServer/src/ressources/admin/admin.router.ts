import { Router } from 'express';

import {
  getAllSurveys,
  getQuestionsBySurveyId,
  getAnswers,
  getOneSurvey,
  updateOneSurvey,
  getSingleQuestionById,
  patchSingleQuestionById,
  getAllSurveyCategories,
  getRelatedConditionnal,
  resetDB,
  getAllLabels,
} from './admin.controllers';

const router = Router();

router.route('/surveys').get(getAllSurveys);

router.route('/survey-categories').get(getAllSurveyCategories);

router.route('/survey-labels').get(getAllLabels);

router.route('/survey-related-conditional/:id').get(getRelatedConditionnal);

router.route('/surveys/:id').get(getOneSurvey);

router.route('/surveys/:id').patch(updateOneSurvey);

router.route('/questions/:id').get(getQuestionsBySurveyId);

router.route('/question/:id').get(getSingleQuestionById);

router.route('/question/:id').patch(patchSingleQuestionById);

router.route('/answers').get(getAnswers);

router.route('/reset').get(resetDB);

export default router;
