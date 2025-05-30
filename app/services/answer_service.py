from app.models.answer_model import Answer
from app.database import db

class AnswerService:
    @staticmethod
    def get_all():
        return Answer.query.all()

    @staticmethod
    def get_by_id(id):
        return Answer.query.get(id)

    @staticmethod
    def create(question_id, data):
        answer = Answer(answer_text=data['answer_text'], question_id=question_id)
        db.session.add(answer)
        db.session.commit()
        return answer

    @staticmethod
    def update(id, data):
        answer = Answer.query.get(id)
        if not answer:
            return None
        answer.answer_text = data.get('answer_text', answer.answer_text)
        db.session.commit()
        return answer

    @staticmethod
    def delete(id):
        answer = Answer.query.get(id)
        if not answer:
            return None
        db.session.delete(answer)
        db.session.commit()
        return True

    @staticmethod
    def get_by_question(question_id):
        return Answer.query.filter_by(question_id=question_id).all()
