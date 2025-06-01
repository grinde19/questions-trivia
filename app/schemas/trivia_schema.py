from app.database import ma
from app.models.trivia_model import Trivia
from app.schemas.question_schema import QuestionSchema

class TriviaSchema(ma.SQLAlchemyAutoSchema):
    questions = ma.Nested(QuestionSchema, many=True)
    
    class Meta:
        model = Trivia
        load_instance = True
        exclude = ['users']

trivia_schema = TriviaSchema()
trivias_schema = TriviaSchema(many=True)
