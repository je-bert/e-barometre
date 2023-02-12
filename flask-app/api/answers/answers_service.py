
from flask import request, jsonify
from models import Question

def update():
  #TODO: use real user_id
  user_id = 0
  json = request.json
  if not 'answers' in json:
    return "Erreur", 400

  for answer in json['answers']:
    if not 'question_id' in answer:
      return "Erreur", 400

    question = Question.query\
        .filter_by(question_id = answer['question_id'])\
        .first()
    
    if not question:
      return "Erreur", 400 
    
  return jsonify("Vos réponses ont été sauvegardées!"), 200

#   export const put = async (req, res) => {
#   // const user = res.locals.user;

#   const user = { user_id: 1 };

#   if (!req.body || !req.body.answers)
#     return res
#       .status(400)
#       .json({ message: "Le format de la requête n'est pas valide." });

#   for (let i = 0; i < req.body.answers.length; i++) {
#     const { question_id, value, custom_answer } = answer;

#     if (
#       !question_id ||
#       typeof question_id !== "string" ||
#       !value ||
#       typeof value !== "string"
#     )
#       return res.status(400).json({
#         message: `Le format de la réponse à l'index ${i} n'est pas valide.`,
#       });

#     const question = await db.get(
#       `SELECT [question_id], [type], [label_id], [order], [min_value], [max_value] FROM question WHERE question_id = ?`,
#       question_id
#     );

#     if (!question)
#       return res
#         .status(400)
#         .json({ message: `La question '${question_id}' n'existe pas.` });

#     switch (question.type) {
#       case "numeric-ladder":
#         if (!Number.isInteger(+value) || +value < 0 || +value > 10) {
#           return res.status(400).json({
#             message: `Le choix de réponse '${value}' n'est pas valide pour la question à échelle numérique '${question_id}'.`,
#           });
#         }
#         break;
#       case "integer":
#         if (
#           !Number.isInteger(+value) ||
#           +value < question.min_value ||
#           +value > question.max_value
#         ) {
#           return res.status(400).json({
#             message: `Le choix de réponse '${value}' n'est pas valide pour la question à nombre entier '${question_id}'.`,
#           });
#         }
#         break;
#       case "labeled-ladder":
#         const label = await db.get(
#           `SELECT [label_id], [value] FROM label WHERE label_id = ? AND value = ?`,
#           question.label_id,
#           value
#         );
#         if (!label) {
#           return res.status(400).json({
#             message: `Le choix de réponse '${value}' n'est pas valide pour la question à échelle étiquettée '${question_id}'.`,
#           });
#         }
#         break;
#       case "select-single":
#         const choice = await db.get(
#           `SELECT [question_id], [value] FROM choice WHERE question_id = ? AND value = ?`,
#           question_id,
#           value
#         );
#         if (!choice) {
#           return res.status(400).json({
#             message: `Le choix de réponse '${value}' n'est pas valide pour la question à sélection simple '${question_id}'.`,
#           });
#         }
#         if (custom_answer) {
#           if (typeof custom_answer !== "string")
#             return res.status(400).json({
#               message: `Le format de la réponse personnalisée de la question ${question_id} n'est pas valide.`,
#             });

#           if (value !== "custom") {
#             return res.status(400).json({
#               message: `Une réponse personnalisée a été spécifiée, mais le choix ne le permet pas.`,
#             });
#           }
#           await db.exec(
#             `REPLACE INTO custom_answer (question_id, user_id, value, date_created) VALUES('${question_id}', '${user.user_id}', '${custom_answer}',DATE('now'))`
#           );
#         }
#         break;
#       case "select-multiple":
#         const answers = value.split(",");
#         if (answers.includes(""))
#           return res.status(400).json({
#             message: `Le choix de réponse '${value}' n'est pas valide pour la question à sélection multiple '${question_id}'.`,
#           });

#         const placeHolders = new Array(answers.length).fill("?").join(",");
#         const query = `SELECT [question_id], [value] FROM choice WHERE question_id = ? AND value IN (${placeHolders})`;
#         const choices = await db.all(query, [question_id, ...answers]);
#         if (!choices || answers.length != choices.length) {
#           return res.status(400).json({
#             message: `Le choix de réponse '${value}' n'est pas valide pour la question à sélection multiple '${question_id}'.`,
#           });
#         }
#         if (custom_answer) {
#           if (typeof custom_answer !== "string")
#             return res.status(400).json({
#               message: `Le format de la réponse personnalisée de la question ${question_id} n'est pas valide.`,
#             });

#           if (!answers.includes("custom")) {
#             return res.status(400).json({
#               message: `Une réponse personnalisée a été spécifiée, mais le choix ne le permet pas.`,
#             });
#           }
#           await db.exec(
#             `REPLACE INTO custom_answer (question_id, user_id, value, date_created) VALUES('${question_id}', '${user.user_id}', '${custom_answer}',DATE('now'))`
#           );
#         }
#         break;
#       case "binary":
#         if (value !== "TRUE" && value !== "FALSE") {
#           return res.status(400).json({
#             message: `Le choix de réponse '${value}' n'est pas valide pour la question binaire '${question_id} (doit être 'TRUE' ou 'FALSE').`,
#           });
#         }
#         break;
#       default:
#         return res.status(400).json({
#           message: `Le type de la question '${question_id}' n'existe pas.`,
#         });
#     }
#   }

#   for (let i = 0; i < req.body.answers.length; i++) {
#     await db.exec(
#       `REPLACE INTO answer (question_id, user_id, value, date_created) VALUES('${req.body.answers[i].question_id}', '${user.user_id}', '${req.body.answers[i].value}',DATE('now'))`
#     );
#   }

#   return res.status(200).json({
#     message: "Vos réponses ont été sauvegardées!",
#   });
# };
