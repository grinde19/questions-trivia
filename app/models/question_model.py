from app.database import db
from app.models.trivia_question_inter import trivia_question

class Question(db.Model):
    __tablename__ = 'questions'
    
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(255), nullable=False)

    # Foreign Keys
    trivia_id = db.Column(db.Integer, db.ForeignKey('trivia.id'), nullable=False)
    level_id = db.Column(db.Integer, db.ForeignKey('level.id'), nullable=False)
    
    # Relaciones
    trivia = db.relationship('Trivia', back_populates='questions')
    level = db.relationship('Level', back_populates='questions')
    answers = db.relationship('Answer', back_populates='question', cascade='all, delete-orphan')
