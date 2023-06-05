import { db } from "../../db";

export const getAll = async (req, res) => {
  const data = await db.all(`SELECT * FROM survey WHERE status = 'active'`);

  if (!data)
    return res.status(400).json({
      message: `Unable to fetch the surveys.`,
    });

  return res.status(200).json(data);
};

export const getById = async (req, res) => {
  const user = res.locals.user;

  const data = await db.get(
    `SELECT [survey_id], [name], [description], [color], [cover_picture_url] FROM survey WHERE survey_id = '${req.params.id}' AND status = 'active' LIMIT 1`
  );

  if (!data)
    return res.status(400).json({
      message: `Unable to find the survey with id $${req.params.id}.`,
    });

  data.is_available = true; // TODO: Look depending on user's answers
  data.is_completed = false; // TODO: Look depending on user's answers

  data.questions = await db.all(
    `SELECT [question_id], [title],[intro], [type], [label_id], [info_bubble_text], [condition], [order], [min_value], [max_value] FROM question WHERE survey_id = '${req.params.id}' ORDER BY [order]`
  );

  for (let i = 0; i < data.questions.length; i++) {
    const choices = await db.all(
      data.questions[i].type === "labeled-ladder"
        ? `SELECT [value], [label] FROM label WHERE label_id = '${data.questions[i].label_id}' ORDER BY [order]`
        : `SELECT [value], [label] FROM choice WHERE question_id = '${data.questions[i].question_id}' ORDER BY [order]`
    );

    if (choices.length > 0) data.questions[i].choices = choices;

    const answer = await db.get(
      `SELECT [value] FROM answer WHERE question_id = '${
        data.questions[i].question_id
      }' AND user_id = '${1 || user.user_id}' LIMIT 1`
    );

    if (answer) {
      data.questions[i].answer = answer.value;
      if (answer.value.split(",").includes("custom")) {
        const custom_answer = await db.get(
          `SELECT [value] FROM custom_answer WHERE question_id = '${data.questions[i].question_id}' AND user_id = '${user.user_id}' LIMIT 1`
        );
        if (custom_answer)
          data.questions[i].custom_answer = custom_answer.value;
      }
    }
  }

  return res.json(data);
};
