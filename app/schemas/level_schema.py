from app.database import ma
from app.models.level_model import Level

class LevelSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Level
        load_instance = True
        exclude = ['questions']

level_schema = LevelSchema()
levels_schema = LevelSchema(many=True)
