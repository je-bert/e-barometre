import * as path from 'path';
import * as util from 'util';
import * as fs from 'fs';

const sqlite3 = require('sqlite3').verbose();

const DB_PATH = path.join(__dirname, 'my.db');

const DB_SQL_PATH = path.join(__dirname, 'init.sql');
const SEED_SQL_PATH = path.join(__dirname, 'seed.sql');
const SEED_QUESTION_CATEGORY_PATH = path.join(
  __dirname,
  'seeds',
  'question_category.sql'
);

const SEED_QUESTION_CONDITION_PATH = path.join(
  __dirname,
  'seeds',
  'question_condition.sql'
);

const SEED_QUESTION_PAST_TITLE_PATH = path.join(
  __dirname,
  'seeds',
  'past_title.sql'
);

const SEEQ_QUESTION_TITLE_CORRECTIONS_PATH = path.join(
  __dirname,
  'seeds',
  'question_title_corrections.sql'
);

const myDB = new sqlite3.Database(DB_PATH);

const db = {
  run(...args: any[]): Promise<{ changes: number; lastID: number } | null> {
    return new Promise(function c(resolve, reject) {
      myDB.run(...args, function onResult(err: any) {
        if (err) reject(err);
        //@ts-ignore
        else resolve(this);
      });
    });
  },
  get: util.promisify(myDB.get.bind(myDB)),
  all: util.promisify(myDB.all.bind(myDB)),
  exec: util.promisify(myDB.exec.bind(myDB)),

  async isOk(...args: any[]): Promise<boolean> {
    const result = await this.run(...args);

    return result != null && result.changes > 0;
  },
};

const initSQL = fs.readFileSync(DB_SQL_PATH, 'utf-8');

const seedSQL = fs.readFileSync(SEED_SQL_PATH, 'utf-8');

const seedQuestionCategory = fs.readFileSync(
  SEED_QUESTION_CATEGORY_PATH,
  'utf-8'
);

const seedQuestionCondition = fs.readFileSync(
  SEED_QUESTION_CONDITION_PATH,
  'utf-8'
);

const seedPastTitle = fs.readFileSync(SEED_QUESTION_PAST_TITLE_PATH, 'utf-8');

const seedQuestionCorrections = fs.readFileSync(
  SEEQ_QUESTION_TITLE_CORRECTIONS_PATH,
  'utf-8'
);

async function init() {
  console.log('database init!');
  let err = false;

  try {
    await db.exec(initSQL);
    await db.exec(seedQuestionCategory);

    await db.exec(seedSQL);

    await db.exec(seedQuestionCondition);
    await db.exec(seedPastTitle);
    await db.exec(seedQuestionCorrections);
  } catch (error) {
    err = true;
    console.log('Error while created the database', error);
  }

  return err;
}

export { init, db };
