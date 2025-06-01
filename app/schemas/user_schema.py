from app.database import ma
from app.models.user_model import User
from app.schemas.role_schema import RoleSchema
from app.schemas.trivia_summary_schema import TriviaSummarySchema

class UserSchema(ma.SQLAlchemyAutoSchema):
    roles = ma.Nested(RoleSchema, many=True)
    trivias = ma.Nested(TriviaSummarySchema, many=True)
    
    class Meta:
        model = User
        load_instance = True
        exclude = ['password_hash']

user_schema = UserSchema()
users_schema = UserSchema(many=True)
