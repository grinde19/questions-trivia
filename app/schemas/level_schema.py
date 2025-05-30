from flask_marshmallow import Marshmallow
from app.models.level_model import Level

ma = Marshmallow()

class LevelSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Level
        load_instance = True
