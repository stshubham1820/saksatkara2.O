from rest_framework import serializers
from assessment.models import AssessmentQuestions,AssessmentAnswers

class AssessmentQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = AssessmentQuestions
        fields = '__all__'

class AssessmentAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = AssessmentAnswers
        fields = '__all__'