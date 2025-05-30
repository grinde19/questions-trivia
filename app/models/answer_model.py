from app.database import db

class Answer(db.Model):
    __tablename__ = 'answers'

    id = db.Column(db.Integer, primary_key=True)
    answer_text = db.Column(db.String(255), nullable=False)
    answer_right = db.Column(db.Boolean, default=False)  # <-- VALIDAR SEA UN TRUE POR TABLE

    question_id = db.Column(db.Integer, db.ForeignKey('questions.id'), nullable=False)
