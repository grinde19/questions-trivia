from flask import request, abort, jsonify
from app.services.role_service import RoleService

def list_roles():
    roles = RoleService.get_all_roles()
    return jsonify([{"id": r.id, "name": r.name} for r in roles]), 200

def create_role():
    data = request.get_json()
    name = data.get('name')
    if not name:
        abort(400, 'Nombre requerido')
    role = RoleService.create_role(name)
    return jsonify({"id": role.id, "name": role.name}), 201
