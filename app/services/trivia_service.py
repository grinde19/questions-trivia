from app.database import db
from app.models.trivia import Trivia
from app.models.question import Question

class TriviaService:

    @staticmethod
    def get_all_trivias():
        return Trivia.query.all()

    @staticmethod
    def get_trivia_by_id(trivia_id):
        return Trivia.query.get(trivia_id)

    @staticmethod
    def create_trivia(nombre):
        trivia = Trivia(nombre=nombre)
        db.session.add(trivia)
        db.session.commit()
        return trivia

    @staticmethod
    def update_trivia(trivia, nombre=None, question_ids=None):
        if nombre:
            trivia.nombre = nombre
        if question_ids is not None:
            # Filtrar preguntas que existen en la BD y están en la lista recibida
            questions = Question.query.filter(Question.id.in_(question_ids)).all()

            # Aquí podrías validar que todas las question_ids existen
            if len(questions) != len(question_ids):
                missing = set(question_ids) - {q.id for q in questions}
                raise ValueError(f"Las siguientes preguntas no existen: {missing}")

            # Actualizar la relación con las preguntas válidas
            trivia.questions = questions

        db.session.commit()
        return trivia


    @staticmethod
    def delete_trivia(trivia):
        db.session.delete(trivia)
        db.session.commit()
