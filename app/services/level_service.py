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
        level.text = data.get('text', level.text)
        level.poiny = data.get('point', level.point)
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
