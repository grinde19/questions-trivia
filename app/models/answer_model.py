from app.database import db

class Answer(db.Model):
    __tablename__ = 'answers'

    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(255), nullable=False)
    is_correct = db.Column(db.Boolean, default=False)  # TO DO<-- VALIDAR SEA UN TRUE POR TABLE

    # Foreign Key
    question_id = db.Column(db.Integer, db.ForeignKey('question.id'), nullable=False)
    
    # Relaciones
    question = db.relationship('Question', back_populates='answers')
