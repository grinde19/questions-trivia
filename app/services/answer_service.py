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
        ## TO DO validar si el is_correct esta en boolean
        answer = Answer(text=data['text'], question_id=question_id, is_correct=data['is_correct'])
        db.session.add(answer)
        db.session.commit()
        return answer

    @staticmethod
    def update(id, data):
        answer = Answer.query.get(id)
        if not answer:
            return None
        ## TO DO debo actualizar el is_correct, por defecto es false    
        answer.text = data.get('text', answer.text)
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
