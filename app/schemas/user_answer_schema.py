from marshmallow import Schema, fields
from app.database import ma
from app.models.user_answer_model import UserAnswer

class UserAnswerSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = UserAnswer
        load_instance = True

user_answer_schema = UserAnswerSchema()
users_answers_schema = UserAnswerSchema(many=True)

# Schema auxiliar para validar una respuesta individual
class SingleResponseSchema(Schema):
    question_id = fields.Int(required=True)
    answer_id = fields.Int(required=True)

# Validador de input completo: user_id, trivia_id, responses[]
class SubmitAnswersSchema(Schema):
    user_id = fields.Int(required=True)
    trivia_id = fields.Int(required=True)
    responses = fields.List(fields.Nested(SingleResponseSchema), required=True)