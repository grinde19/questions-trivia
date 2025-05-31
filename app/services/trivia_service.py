from app.database import db
from app.models.trivia import Trivia
from app.models.question import Question

class TriviaService:

    @staticmethod
    def get_all():
        return Trivia.query.all()

    @staticmethod
    def get_by_id(trivia_id):
        return Trivia.query.get(trivia_id)

    @staticmethod
    def create(name):
        trivia = Trivia(text=name)
        db.session.add(trivia)
        db.session.commit()
        return trivia

    @staticmethod
    def update(trivia, name=None, question_ids=None):
        if name:
            trivia.text = name
        if question_ids is not None:
            # Filtrar preguntas que existen en la BD y están en la lista recibida
            questions = Question.query.filter(Question.id.in_(question_ids)).all()

            # validar que todas las question_ids existen
            if len(questions) != len(question_ids):
                missing = set(question_ids) - {q.id for q in questions}
                raise ValueError(f"Las siguientes preguntas no existen: {missing}")

            # Actualizar la relación con las preguntas válidas
            trivia.questions = questions

        db.session.commit()
        return trivia

    @staticmethod
    def delete(trivia):
        db.session.delete(trivia)
        db.session.commit()
