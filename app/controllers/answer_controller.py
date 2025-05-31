from flask import request
from app.services.answer_service import AnswerService
from app.schemas.answer_schema import answer_schema, answers_schema

def get_answers():
    return answers_schema.jsonify(AnswerService.get_all())

def get_answer(id):
    answer = AnswerService.get_by_id(id)
    if not answer:
        return {"message": "Respuesta no encontrada"}, 404
    return answer_schema.jsonify(answer)

def create_answer(question_id):
    data = request.get_json()
    answer = AnswerService.create(question_id, data)
    return answer_schema.jsonify(answer), 201

def update_answer(id):
    data = request.get_json()
    answer = AnswerService.update(id, data)
    if not answer:
        return {"message": "Respuesta no encontrada"}, 404
    return answer_schema.jsonify(answer)

def delete_answer(id):
    deleted = AnswerService.delete(id)
    if not deleted:
        return {"message": "Respuesta no encontrada"}, 404
    return {"message": "Respuesta eliminada"}

def get_answers_by_question(question_id):
    return answers_schema.jsonify(AnswerService.get_by_question(question_id))
