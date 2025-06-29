from app.database import ma
from app.models.role_model import Role

class RoleSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Role
        load_instance = True
        exclude = ['users']

role_schema = RoleSchema()
roles_schema = RoleSchema(many=True)
