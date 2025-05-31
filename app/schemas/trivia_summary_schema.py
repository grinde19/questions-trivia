class TriviaSummarySchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Trivia
        load_instance = True
        fields = ['id', 'text']

trivia_summary_schema = TriviaSummarySchema()
trivias_summary_schema = TriviaSummarySchema(many=True)
