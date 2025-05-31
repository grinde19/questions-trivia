from app.database import db
from app.models.trivia_question_inter import trivia_question
from app.models.user_trivia_inter import user_trivia

class Trivia(db.Model):
    __tablename__ = 'trivias'

    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(150), nullable=False)

    # Relaciones
    questions = db.relationship('Question', back_populates='trivia', cascade='all, delete-orphan')
    users = db.relationship('User', secondary=user_trivia, back_populates='trivias')
