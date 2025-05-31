from flask import request, abort, jsonify
from app.services.role_service import RoleService
from app.schemas.role_schema import role_schema, roles_schema

def get_all_roles():
    roles = RoleService.get_all()
    return roles_schema.jsonify(roles), 200

def get_role(id):
    role = RoleService.get_by_id(id)
    if not role:
        abort(404, 'Role no encontrado')
    return role_schema.jsonify(role), 200

def create_role():
    data = request.get_json()
    name = data.get('text')
    if not name:
        abort(400, 'El campo texto es requerido.')
    role = RoleService.create(name)
    return role_schema.jsonify(role), 201

def update_role(id):
    role = RoleService.get_by_id(id)
    if not role:
        abort(404, 'Role no encontrado')
    data = request.get_json()
    name = data.get('text')
    try:
        role = RoleService.update(role, name)
    except ValueError as e:
        abort(400, str(e))
    return role_schema.jsonify(role), 200

def delete_role(id):
    deleted = RoleService.delete(id)
    if not deleted:
        return {"message": "Role no encontrado"}, 404
    return {"message": "Role eliminado"}