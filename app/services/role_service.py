from app.database import db
from app.models.role import Role

class RoleService:
    @staticmethod
    def get_all():
        return Role.query.all()

    @staticmethod
    def get_by_id(id):
        return Role.query.get(id)

    @staticmethod
    def create(name):
        role = Role(text=name)
        db.session.add(role)
        db.session.commit()
        return role

    @staticmethod
    def update(role, name=None):
        if name:
            role.text = name
        db.session.commit()
        return role

    @staticmethod
    def delete(role):
        db.session.delete(role)
        db.session.commit()
