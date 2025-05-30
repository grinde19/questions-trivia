from app.database import db

class Level(db.Model):
    __tablename__ = 'levels'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    score = db.Column(db.Integer, nullable=False)

    # Relación 1:N (un nivel tiene muchas preguntas)
    questions = db.relationship('Question', backref='level', lazy=True)
