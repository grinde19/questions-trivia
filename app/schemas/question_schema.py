from app.database import ma
from app.models.question_model import Question
from app.schemas.level_schema import LevelSchema
from app.schemas.answer_schema import AnswerSchema

class QuestionSchema(ma.SQLAlchemyAutoSchema):
    level = ma.Nested(LevelSchema)
    answers = ma.Nested(AnswerSchema, many=True)

    class Meta:
        model = Question
        load_instance = True
        exclude = ['trivia'] 

question_schema = QuestionSchema()
questions_schema = QuestionSchema(many=True)