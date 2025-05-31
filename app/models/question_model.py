from app.database import db
from app.models.trivia_question_inter import trivia_question

class Question(db.Model):
    __tablename__ = 'questions'
    
    id = db.Column(db.Integer, primary_key=True)
    question_text = db.Column(db.String(255), nullable=False)

    # Relacion con Level -> foreingKEy
    level_id = db.Column(db.Integer, db.ForeignKey('levels.id'), nullable=False)

    # Relación con Answer -> 1:N
    answers = db.relationship('Answer', backref='question', cascade="all, delete", lazy=True)

    # Relación con Trivia -> N:N
    trivias = db.relationship(
        'Trivia',
        secondary=trivia_question,
        back_populates='questions'
    )
