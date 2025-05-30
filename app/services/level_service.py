from app.models.level_model import Level
from app.database import db

class LevelService:
    @staticmethod
    def get_all():
        return Level.query.all()

    @staticmethod
    def get_by_id(id):
        return Level.query.get(id)

    @staticmethod
    def create(data):
        level = Level(**data)
        db.session.add(level)
        db.session.commit()
        return level

    @staticmethod
    def update(id, data):
        level = Level.query.get(id)
        if not level:
            return None
        level.nombre = data.get('nombre', level.nombre)
        level.puntaje = data.get('puntaje', level.puntaje)
        db.session.commit()
        return level

    @staticmethod
    def delete(id):
        level = Level.query.get(id)
        if not level:
            return None
        db.session.delete(level)
        db.session.commit()
        return True
