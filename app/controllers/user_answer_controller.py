from flask import request, jsonify
from marshmallow import ValidationError
from app.services.user_answer_service import UserAnswerService
from app.schemas.user_answer_schema import user_answer_schema,users_answers_schema, SubmitAnswersSchema
from app.schemas.trivia_points_schema import trivia_stats_schema

def create_all_answer():
    data = request.get_json()

    #Validando usando los schemas 
    try:
        validated_data = SubmitAnswersSchema().load(data)
    except ValidationError as err:
        return {'errors': err.messages}, 400

    user_id = validated_data['user_id']
    trivia_id = validated_data['trivia_id']
    response = validated_data['responses']

    values = UserAnswerService.create_user_response(user_id, trivia_id, response)
    return user_answer_schema.jsonify(values), 201


def get_users_trivia_stats(trivia_id):
    result = UserAnswerService.get_user_stats_by_trivia(trivia_id)
    return jsonify(trivia_stats_schema.dump(result)), 200