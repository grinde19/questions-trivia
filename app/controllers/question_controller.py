from flask import request
from app.services.question_service import QuestionService
from app.schemas.question_schema import question_schema, questions_schema

def get_questions():
    return questions_schema.jsonify(QuestionService.get_all())

def get_question(id):
    question = QuestionService.get_by_id(id)
    if not question:
        return {"message": "Pregunta no encontrada"}, 404
    return question_schema.jsonify(question)

def create_question():
    data = request.get_json()
    question = QuestionService.create(data)
    return question_schema.jsonify(question), 201

def update_question(id):
    data = request.get_json()
    question = QuestionService.update(id, data)
    if not question:
        return {"message": "Pregunta no encontrada"}, 404
    return question_schema.jsonify(question)

def delete_question(id):
    deleted = QuestionService.delete(id)
    if not deleted:
        return {"message": "Pregunta no encontrada"}, 404
    return {"message": "Pregunta eliminada"}

def get_questions_by_level(level_id):
    return questions_schema.jsonify(QuestionService.get_by_level(level_id))

def get_questions_by_trivia(trivia_id):
    return questions_schema.jsonify(QuestionService.get_by_trivia(trivia_id))