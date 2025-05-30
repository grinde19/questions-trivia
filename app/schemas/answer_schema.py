from flask_marshmallow import Marshmallow
from app.models.answer_model import Answer

ma = Marshmallow()

class AnswerSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Answer
        load_instance = True
