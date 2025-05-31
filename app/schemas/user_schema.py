from app.database import ma
from app.models.user import User
from app.schemas.role_schema import RoleSchema  # importar desde otro archivo

class UserSchema(ma.SQLAlchemyAutoSchema):
    roles = ma.Nested(RoleSchema, many=True)

    class Meta:
        model = User
        load_instance = True

user_schema = UserSchema()
users_schema = UserSchema(many=True)
