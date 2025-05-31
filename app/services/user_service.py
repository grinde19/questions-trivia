from app.database import db
from app.models.user import User
from app.models.role import Role

class UserService:
    @staticmethod
    def get_all_users():
        return User.query.all()

    @staticmethod
    def get_user_by_id(user_id):
        return User.query.get(user_id)

    @staticmethod
    def create_user(name, email):
        user = User(name=name, email=email)
        db.session.add(user)
        db.session.commit()
        return user

    @staticmethod
    def update_user(user, name=None, email=None):
        if name:
            user.name = name
        if email:
            user.email = email
        db.session.commit()
        return user

    @staticmethod
    def delete_user(user):
        db.session.delete(user)
        db.session.commit()

    @staticmethod
    def assign_roles(user, role_ids):
        roles = Role.query.filter(Role.id.in_(role_ids)).all()
        if len(roles) != len(role_ids):
            raise ValueError("Uno o más roles no existen")
        user.roles = roles  # se asignan (reemplazan) los roles actuales
        db.session.commit()
        return user
