from app.database import ma
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from app.models.trivia import Trivia
from app.schemas.question_schema import QuestionSchema

class TriviaSchema(SQLAlchemyAutoSchema):
    questions = ma.Nested(QuestionSchema, many=True)

    class Meta:
        model = Trivia
        load_instance = True
        include_relationships = True
