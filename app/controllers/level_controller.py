from flask import request
from app.services.level_service import LevelService
from app.schemas.level_schema import level_schema, levels_schema


def get_levels():
    levels = LevelService.get_all()
    return levels_schema.jsonify(levels)

def get_level(id):
    level = LevelService.get_by_id(id)
    if not level:
        return {"message": "Nivel no encontrado"}, 404
    return level_schema.jsonify(level)

def create_level():
    data = request.get_json()
    level = LevelService.create(data)
    return level_schema.jsonify(level), 201

def update_level(id):
    data = request.get_json()
    level = LevelService.update(id, data)
    if not level:
        return {"message": "Nivel no encontrado"}, 404
    return level_schema.jsonify(level)

def delete_level(id):
    deleted = LevelService.delete(id)
    if not deleted:
        return {"message": "Nivel no encontrado"}, 404
    return {"message": "Nivel eliminado"}
