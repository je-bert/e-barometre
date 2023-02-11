import { RequestHandler } from 'express';
import { db, init } from '../../db';

export const getAllSurveyCategories: RequestHandler = async (req, res) => {
  const data = await db.all(`
  
    SELECT [category_id] from question_category
  `);

  res.json(data);
};

export const getOneSurvey: RequestHandler = async (req, res) => {
  const data = await db.get(
    `SELECT [survey_id], [name], [description], [color], [cover_picture_url] FROM survey WHERE survey_id = '${req.params.id}' LIMIT 1`
  );

  data.questions = await db.all(
    `SELECT

    q.[question_id],
    q.[intro],
    q.[title],
    q.[type], 
    q.[label_id],
    q.[info_bubble_text], 
    q.[condition],
    q.[intensity], 
    q.[order],
    q.[min_value],
    q.[max_value],
    q.[ladderC],
    q.[ladderE],
    q.[ladderV],
    
    qcc.[category_id] as category
    
    FROM question as q 
    
    left outer join question_category_question as qcc on qcc.question_id = q.question_id

    


    WHERE q.survey_id = '${req.params.id}'
    
    
    ORDER BY q.[order]`
  );

  for (let i = 0; i < data.questions.length; i++) {
    const choices = await db.all(
      data.questions[i].type === 'labeled-ladder'
        ? `SELECT [value], [label] FROM label WHERE label_id = '${data.questions[i].label_id}' ORDER BY [order]`
        : `SELECT [value], [label] FROM choice WHERE question_id = '${data.questions[i].question_id}' ORDER BY [order]`
    );

    if (choices.length > 0) data.questions[i].choices = choices;
  }

  res.json(data);
};

export const getAllSurveys: RequestHandler = async (req, res) => {
  const data = await db.all(`

  SELECT 
  s.[survey_id],
  s.[name],
  s.[description],
  s.[status],
  count(*) as questionCount
  
  FROM survey as s
  
  
  inner join question as q on s.survey_id = q.survey_id

  GROUP BY s.survey_id



  
  `);

  if (data === null || data.length === 0) {
    res.status(404).json({ message: 'no surveys found' });
    return;
  }

  res.status(200).json(data);
};

export const getQuestionsBySurveyId: RequestHandler = async (req, res) => {
  const data = await db.all(
    `
		SELECT 
			q.question_id,
			q.title,
			q.type,
			q.label_id,
			q.info_bubble_text,
			q.condition,
			q.intensity,
			q.min_value,
			q.max_value,
      q.active,
      q.violence_related

			case q.type 
				when 'select-single' then 

					JSON_GROUP_ARRAY(JSON_OBJECT(coalesce(c.label,'todo'),c.value))

				when 'select-multiple' then 

					JSON_GROUP_ARRAY(JSON_OBJECT(coalesce(c.label,'todo'),c.value))

				when 'labeled-ladder' then 

					JSON_GROUP_ARRAY(JSON_OBJECT(coalesce(l.label,'todo'),l.value))

				else null
				
			end as choices 


		FROM question AS q

	
		LEFT JOIN choice as c on q.question_id = c.question_id 
		LEFT JOIN label as l on q.label_id = l.label_id 
	

		where q.survey_id = ? 

		GROUP BY q.question_id

	`,
    [req.params.id]
  );

  return res.status(200).json(data);
};

export const getAnswers: RequestHandler = async (req, res) => {
  const data = await db.all(`
		SELECT * FROM answer UNION SELECT * FROM custom_answer
	`);

  res.status(200).json(data);
};

export const updateOneSurvey: RequestHandler = async (req, res) => {
  const { name, description, status, color } = req.body;

  if (req.params.id === undefined) {
    res.status(400).json({ message: 'no survey id provided' });
    return;
  }

  const updatedSurveyQuery = await db.run(
    `
		UPDATE survey SET name = ?, description = ?, status = ?, color = ? WHERE survey_id = ?
  `,
    [name, description, status, color, req.params.id]
  );

  if (updatedSurveyQuery === null) {
    res.status(404).json({ message: 'survey not found' });
    return;
  }

  return res.status(200).json({ message: 'survey updated' });
};

export const getSingleQuestionById: RequestHandler = async (req, res) => {
  const id = req.params.id;

  const question = await db.get(
    `
		SELECT * FROM question WHERE question_id = ?
  `,
    [id]
  );

  if (question === null) {
    res.status(404).json({ message: 'question not found' });
    return;
  }

  return res.status(200).json(question);
};

export const patchSingleQuestionById: RequestHandler = async (req, res) => {
  const id = req.params.id;

  const {
    title,
    info_bubble_text,
    intensity,
    condition,
    intro,
    ladderC,
    ladderE,
    ladderV,
    categorie,
  } = req.body;

  const updatedQuestion = await db.run(
    `
		UPDATE question SET
     title = ?,
      intro = ?,
       info_bubble_text = ?,
        intensity = ?,
         condition = ?,
          ladderC = ?,
           ladderE = ?,
            ladderV = ?,
             categorie = ?
              WHERE question_id = ?
		`,
    [
      title,
      intro,
      info_bubble_text,
      intensity,
      condition,
      ladderC,
      ladderE,
      ladderV,
      categorie,
      id,
    ]
  );

  if (updatedQuestion === null) {
    res.status(404).json({ message: 'question not found' });
    return;
  }

  res.status(200).json({ message: 'question updated' });
};

export const getRelatedConditionnal: RequestHandler = async (req, res) => {
  // todo cache the values or create separate tables

  const { id } = req.params;

  const conditions = await db.all(
    `SELECT * from condition where [left_operand]=?`,
    [id]
  );

  res.json(conditions);
};

export const resetDB: RequestHandler = async (req, res) => {
  await init();

  res.status(200).json({ message: 'database reset' });
};

export const getAllLabels: RequestHandler = async (req, res) => {
  const distinctLabelIds: { label_id: string }[] = await db.all(
    `SELECT DISTINCT label_id FROM label`
  );

  const labels: { label_id: string; value: number | null; label: string }[] =
    await db.all(`SELECT label_id,value,label FROM label`);

  const payload = distinctLabelIds.reduce((acc, { label_id }) => {
    acc.push({
      name: label_id,
      values: labels.reduce((acc, label) => {
        if (label.label_id === label_id) {
          acc.push({ value: label.value, label: label.label });
        }
        return acc;
      }, [] as { value: number | null; label: string }[]),
    });

    return acc;
  }, [] as { name: string; values: { value: number | null; label: string }[] }[]);

  res.json(payload);
};
