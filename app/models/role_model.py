from app.database import db
from app.models.user_roles_inter import user_roles

class Role(db.Model):
    __tablename__ = 'roles'

    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(50), unique=True, nullable=False)

    users = db.relationship('User', secondary=user_roles, back_populates='roles')
