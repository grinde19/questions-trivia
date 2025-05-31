from app.database import db

user_trivia = db.Table('user_trivia',
    db.Column('user_id', db.Integer, db.ForeignKey('users.id'), primary_key=True),
    db.Column('trivia_id', db.Integer, db.ForeignKey('trivias.id'), primary_key=True)
)
