from app.database import db
from app.models.user_roles_inter import user_roles
from app.models.user_trivia_inter import user_trivia

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password_hash = db.Column(db.String(128))

    roles = db.relationship('Role', secondary=user_roles, back_populates='users')
    trivias = db.relationship('Trivia', secondary=user_trivia, back_populates='users')
