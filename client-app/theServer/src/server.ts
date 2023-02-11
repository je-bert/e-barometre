import 'dotenv/config';
const express = require('express');
const cors = require('cors');

import { Application } from 'express';

import { init } from './db';
import { signIn, signUp } from './utils/auth';

import surveyRouter from './ressources/survey/survey.router';
import answerRouter from './ressources/answer/answer.router';
import adminRouter from './ressources/admin/admin.router';

const PORT = 3000;

const app: Application = express();

app.use(cors());
app.use(express.json());
app.post('/api/auth/sign-up', signUp);
app.post('/api/auth/sign-in', signIn);

// app.use('/api', protect);
app.use('/api/survey', surveyRouter);
app.use('/api/answer', answerRouter);

app.use('/api/admin', adminRouter);

init()
  .then(() =>
    app.listen(PORT, () => console.log(`server started on port ${PORT}`))
  )
  .catch((e: any) => {
    console.log(e);
  });

// use to reset db while we are developing do not remove

app.get('/api/boom', (req, res) => {
  init()
    .then(() => {
      res.status(200).json({ message: 'boom' });
    })
    .catch(() => {
      res.status(500).json({ message: 'something went wrong' });
    });
});
