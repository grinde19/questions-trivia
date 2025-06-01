from marshmallow import Schema, fields

class TriviaStatsSchema(Schema):
    user_id = fields.Int(required=True)
    total_questions = fields.Int(required=True)
    answered_questions = fields.Int(required=True)
    total_points = fields.Int(required=True)
    correct_answers = fields.Int(required=True)
    wrong_answers = fields.Int(required=True)

trivia_stats_schema = TriviaStatsSchema(many=True)
