import * as fs from 'fs';
import { parse } from 'csv-parse';

const dataSrc = 'data-RAW.csv';

if (fs.existsSync('data-CLEAN.json')) {
  fs.rmSync('data-CLEAN.json');
}

fs.writeFileSync('data-CLEAN.json', '[');

const writeStream = fs.createWriteStream('data-CLEAN.json', { flags: 'a' });

const readStream = fs
  .createReadStream(dataSrc, 'utf-8')
  .pipe(parse({ delimiter: ',' }));

readStream.on('data', (dataRow) => {
  const question_id = dataRow[6];
  const question_title = dataRow[9];
  let choices = dataRow[10];
  let type = dataRow[16];
  const survey_id = question_id.split(/\d/)[0];
  const info_bubble_text = dataRow[36];

  choices = choices.split('\r\n');

  if (/^E/.test(type)) {
    mutateChoicesBasedOnType(type, choices);
    type = 'labeled-ladder';
  }

  if (/choix multiple|Choix de réponses|Choix multiples/.test(type)) {
    type = 'multiple-choices';
  }

  if (/1 à 10/.test(type)) {
    type = 'numeric-ladder';
  }
  if (/O\/N/.test(type)) {
    type = 'binary';
  }

  const row = {
    survey_id,
    question_id,
    question_title,
    choices,
    type,
    info_bubble_text,
  };

  if (!question_id) return;

  writeStream.write(JSON.stringify(row) + ',\n');
});

readStream.on('end', () => {
  writeStream.end(']');
});

function mutateChoicesBasedOnType(type: string, choices: string[]) {
  switch (type) {
    case 'E1A':
      choices = [
        'Jamais',
        'Rarement',
        'Parfois',
        'Régulièrement',
        'Souvent',
        'Toujours',
        'S.O.',
      ];

      break;
    case 'E2A':
      choices = [
        'Excellente',
        'Très bonne',
        'Bonne',
        'Moyenne',
        'Mauvaise',
        'Très mauvaise',
        'S.O.',
      ];
      break;
    case 'E3A':
      choices = [
        "Pas du tout d'accord",
        "Pas d'accord",
        "Ni d'accord, ni pas d'accord",
        "Partiellement d'accord",
        "D'accord",
        "Tout à fait d'accord",
        'S.O.',
      ];

      break;
    case 'E4A':
      choices = [
        'Nulle',
        'Très faible',
        'Faible',
        'Moyenne',
        'Élevé',
        'Très élevé',
        'S.O.',
      ];
      break;
    case 'E5A':
      choices = [
        'Au besoin',
        '1 x semaine',
        '3 x semaine',
        '+ de 5 x semaine',
        'tous les jours',
        'plusieurs fois par jour',

        'S.O.',
      ];
      break;

    case 'E6':
      choices = [
        'Pas du tout',
        'Un peu',
        'Normalement',
        'Beaucoup',
        'Énormément',
        'Trop',
        'S.O.',
      ];

      break;

    case 'E1B':
      choices = [
        'Toujours',
        'Souvent',
        'Régulièrement',
        'Parfois',
        'Rarement',
        'Jamais',
        'S.O.',
      ];

      break;

    case 'E2B':
      choices = [
        'Mauvaise',
        'Faible ',
        'Moyenne ',
        'Bonne',
        'Très bonne',
        'Excellente',
        'S.O.',
      ];
      break;

    case 'E3B':
      choices = [
        "Tout à fait d'accord",
        "D'accord",
        "Partiellement d'accord",
        "Ni d'accord, ni pas d'accord",
        "Pas d'accord",
        "Pas du tout d'accord",
        'S.O.',
      ];
      break;

    case 'E4B':
      choices = [
        'Très élevé',
        'Élevé',
        'Moyenne',
        'Faible',
        'Très faible',
        'Nulle',
        'S.O.',
      ];
      break;
  }
}
