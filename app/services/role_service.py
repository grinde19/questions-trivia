from app.database import db
from app.models.role import Role

class RoleService:
    @staticmethod
    def get_all_roles():
        return Role.query.all()

    @staticmethod
    def create_role(name):
        role = Role(name=name)
        db.session.add(role)
        db.session.commit()
        return role
