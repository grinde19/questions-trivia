from flask import request, jsonify, abort
from app.services.trivia_service import TriviaService
from app.schemas.trivia_schema import trivia_schema, trivias_schema

def get_all_trivias():
    trivias = TriviaService.get_all()
    return trivias_schema.jsonify(trivias), 200

def get_trivia(id):
    trivia = TriviaService.get_by_id(id)
    if not trivia:
        abort(404, 'Trivia no encontrada')
    return trivia_schema.jsonify(trivia), 200

def create_trivia():
    data = request.get_json()
    name = data.get('text')
    if not name:
        abort(400, 'El campo texto es requerido.')
    trivia = TriviaService.create(name)
    return trivia_schema.jsonify(trivia), 201

def update_trivia(id):
    trivia = TriviaService.get_by_id(id)
    if not trivia:
        abort(404, 'Trivia no encontrada')
    data = request.get_json()
    name = data.get('text')
    question_ids = data.get('question_ids')
    try:
        trivia = TriviaService.update(trivia, name, question_ids)
    except ValueError as e:
        abort(400, str(e))
    return trivia_schema.jsonify(trivia), 200

def delete_trivia(id):
    deleted = TriviaService.delete(id)
    if not deleted:
        return {"message": "Trivia no encontrada"}, 404
    return {"message": "Trivia eliminada"}