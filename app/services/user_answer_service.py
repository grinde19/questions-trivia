from sqlalchemy import func, case
from app.database import db
from app.models.user_answer_model import UserAnswer
from app.models.answer_model import Answer
from app.models.question_model import Question
from app.models.level_model import Level

class UserAnswerService:
    @staticmethod
    def create_user_response(user_id, trivia_id, responses):
      saved_answers = []

      for item in responses:
          question_id = item['question_id']
          answer_id = item['answer_id']

          # Verificar si la respuesta es correcta
          answer = Answer.query.get(answer_id)
          is_correct = answer.is_correct if answer else False

          user_answer = UserAnswer(
              user_id=user_id,
              trivia_id=trivia_id,
              question_id=question_id,
              answer_id=answer_id,
              is_correct=is_correct
          )

          db.session.add(user_answer)
          saved_answers.append(user_answer)

      db.session.commit()

      return saved_answers

    @staticmethod
    def get_user_stats_by_trivia(trivia_id):
        # 1) Contar cuantas preguntas totales tiene la trivia
        total_questions = (
            db.session.query(func.count(Question.id))
                      .filter(Question.trivia_id == trivia_id)
                      .scalar()
        )

        if total_questions == 0:
            return []

        # 2) Para cada usuario que respondió en esa trivia, calcular las metricas:
        result = (
            db.session.query(
                UserAnswer.user_id,
                func.count(func.distinct(UserAnswer.question_id)).label("answered_questions"),
                func.sum(
                    case(
                        (UserAnswer.is_correct == True, Level.point),
                        else_=0
                    )
                ).label("total_points"),
                func.sum(
                    case(
                        (UserAnswer.is_correct == True, 1),
                        else_=0
                    )
                ).label("correct_answers"),
                func.sum(
                    case(
                        (UserAnswer.is_correct == False, 1),
                        else_=0
                    )
                ).label("wrong_answers"),
            )
            .join(Question, UserAnswer.question_id == Question.id)
            .join(Level, Question.level_id == Level.id)
            .filter(UserAnswer.trivia_id == trivia_id)
            .group_by(UserAnswer.user_id)
            .all()
        )

        return [
            {
                "user_id": row.user_id,
                "total_questions": total_questions,
                "answered_questions": row.answered_questions,
                "correct_answers": row.correct_answers,
                "wrong_answers": row.wrong_answers,
                "total_points": row.total_points,
            }
            for row in result
        ]