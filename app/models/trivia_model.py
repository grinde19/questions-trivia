from app.database import db
from app.models.trivia_question_inter import trivia_question

class Trivia(db.Model):
    __tablename__ = 'trivias'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)

    questions = db.relationship(
        'Question',
        secondary=trivia_question,
        back_populates='trivias'
    )
