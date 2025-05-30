from flask_marshmallow import Marshmallow
from app.models.question_model import Question

ma = Marshmallow()

class QuestionSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Question
        load_instance = True

    #level = ma.Nested(LevelSchema)
    #answers = ma.Nested(AnswerSchema, many=True)