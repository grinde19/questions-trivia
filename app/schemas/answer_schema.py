from app.database import ma
from app.models.answer_model import Answer

class AnswerSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Answer
        load_instance = True
        exclude = ['question']

answer_schema = AnswerSchema()
answers_schema = AnswerSchema(many=True)
