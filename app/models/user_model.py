from app.database import db
from app.models.user_roles_inter import user_roles

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)

    roles = db.relationship('Role', secondary=user_roles, back_populates='users')

    def __repr__(self):
        return f'<User {self.name} ({self.email})>'