from app.database import db

class Level(db.Model):
    __tablename__ = 'levels'

    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(100), nullable=False)
    point = db.Column(db.Integer, default=1)
    
    questions = db.relationship('Question', back_populates='level')
