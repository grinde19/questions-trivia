from app.database import db
from app.models.trivia_model import Trivia
from app.models.question_model import Question
from app.models.user_model import User

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

    @staticmethod
    def add_users(trivia, user_ids=None):
        if user_ids is not None:
            # Filtrar usuarios que existen en la BD y están en la lista recibida
            users = User.query.filter(User.id.in_(user_ids)).all()

            # validar que los  user_ids existen
            if len(users) != len(user_ids):
                missing = set(user_ids) - {u.id for u in users}
                raise ValueError(f"Las siguientes usuarios no existen: {missing}")

            # Actualizar la relación con los usuarios válidas
            print("Usuarios asociados:", trivia.users, flush=True)
            trivia.users = users

        db.session.commit()
        return trivia

    @staticmethod
    def get_users(trivia):
        return trivia.users
