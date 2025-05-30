from flask import request, jsonify, abort
from app.schemas.trivia_schema import TriviaSchema
from app.services.trivia_service import TriviaService

trivia_schema = TriviaSchema()
trivias_schema = TriviaSchema(many=True)

def get_all_trivias():
    trivias = TriviaService.get_all_trivias()
    return trivias_schema.jsonify(trivias), 200

def get_trivia(id):
    trivia = TriviaService.get_trivia_by_id(id)
    if not trivia:
        abort(404, 'Trivia no encontrada')
    return trivia_schema.jsonify(trivia), 200

def create_trivia():
    data = request.get_json()
    nombre = data.get('nombre')
    if not nombre:
        abort(400, 'El campo nombre es requerido.')
    trivia = TriviaService.create_trivia(nombre)
    return trivia_schema.jsonify(trivia), 201

def update_trivia(id):
    trivia = TriviaService.get_trivia_by_id(id)
    if not trivia:
        abort(404, 'Trivia no encontrada')
    data = request.get_json()
    nombre = data.get('nombre')
    question_ids = data.get('question_ids')
    try:
        trivia = TriviaService.update_trivia(trivia, nombre, question_ids)
    except ValueError as e:
        abort(400, str(e))
    return trivia_schema.jsonify(trivia), 200


def delete_trivia(id):
    trivia = TriviaService.get_trivia_by_id(id)
    if not trivia:
        abort(404, 'Trivia no encontrada')
    TriviaService.delete_trivia(trivia)
    return '', 204
