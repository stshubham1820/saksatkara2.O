from rest_framework import serializers
from assessment.models import Assessment,AssessmentCode,AssessmentSkills
from user_authentication.serializers import UserSerializer


class AssessmentCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Assessment
        fields = '__all__'

class AssessmentReadSerializer(serializers.ModelSerializer):

    created_by = UserSerializer(read_only=True)
    assessment_for = UserSerializer(many=True, read_only=True)

    class Meta:
        model = Assessment
        fields = '__all__'

class CodeCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = AssessmentCode
        fields = '__all__'


class AssessmentSkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = AssessmentSkills
        fields = '__all__'