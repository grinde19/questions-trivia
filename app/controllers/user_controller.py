from flask import request, jsonify, abort
from app.services.user_service import UserService
from app.schemas.user_schema import user_schema, users_schema

def list_users():
    users = UserService.get_all_users()
    return users_schema.jsonify(users)

def get_user(id):
    user = UserService.get_user_by_id(id)
    if not user:
        abort(404, 'Usuario no encontrado')
    return user_schema.jsonify(user)

def create_user():
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')
    user = UserService.create_user(name, email)
    return user_schema.jsonify(user), 201

def update_user(id):
    user = UserService.get_user_by_id(id)
    if not user:
        abort(404, 'Usuario no encontrado')
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')
    user = UserService.update_user(user, name, email)
    return user_schema.jsonify(user)

def delete_user(id):
    user = UserService.get_user_by_id(id)
    if not user:
        abort(404, 'Usuario no encontrado')
    UserService.delete_user(user)
    return '', 204

def assign_roles(id):
    user = UserService.get_user_by_id(id)
    if not user:
        abort(404, 'Usuario no encontrado')
    data = request.get_json()
    role_ids = data.get('role_ids', [])
    try:
        user = UserService.assign_roles(user, role_ids)
    except ValueError as e:
        abort(400, str(e))
    return user_schema.jsonify(user)
