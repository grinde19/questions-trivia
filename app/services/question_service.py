from app.models.question_model import Question
from app.database import db

class QuestionService:
    @staticmethod
    def get_all():
        return Question.query.all()

    @staticmethod
    def get_by_id(id):
        return Question.query.get(id)

    @staticmethod
    def create(level_id, data):
        question = Question(question_text=data['question_text'], level_id=level_id)
        db.session.add(question)
        db.session.commit()
        return question

    @staticmethod
    def update(id, data):
        question = Question.query.get(id)
        if not question:
            return None
        question.question_text = data.get('question_text', question.question_text)
        db.session.commit()
        return question

    @staticmethod
    def delete(id):
        question = Question.query.get(id)
        if not question:
            return None
        db.session.delete(question)
        db.session.commit()
        return True

    @staticmethod
    def get_by_level(level_id):
        return Question.query.filter_by(level_id=level_id).all()
