
from app.database import db

class UserAnswer(db.Model):
    __tablename__ = 'user_answers'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    trivia_id = db.Column(db.Integer, db.ForeignKey('trivias.id'), nullable=False)
    question_id = db.Column(db.Integer, db.ForeignKey('questions.id'), nullable=False)
    answer_id = db.Column(db.Integer, db.ForeignKey('answers.id'), nullable=False)
    is_correct = db.Column(db.Boolean, default=False)

    user = db.relationship('User', backref='answers')
    trivia = db.relationship('Trivia', backref='user_answers')
    question = db.relationship('Question', backref='user_answers')
    answer = db.relationship('Answer', backref='user_answers')



