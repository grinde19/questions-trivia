from app.database import db

trivia_question = db.Table(
    'trivia_question',
    db.Column('trivia_id', db.Integer, db.ForeignKey('trivias.id'), primary_key=True),
    db.Column('question_id', db.Integer, db.ForeignKey('questions.id'), primary_key=True)
)
