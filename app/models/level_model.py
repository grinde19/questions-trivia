from app.database import db

class Level(db.Model):
    __tablename__ = 'levels'

    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(100), nullable=False)
    point = db.Column(db.Integer, default=1)

    # Relación 1:N (un nivel puede usarse en muchas preguntas)
    questions = db.relationship('Question', back_populates='level')
