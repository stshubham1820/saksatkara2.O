from rest_framework import serializers
from user_authentication.models import UserSkill


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserSkill
        fields = '__all__'


class RecursiveField(serializers.Serializer):
    def to_representation(self, value):
        # Recursively call the serializer for nested sub-skills
        serializer = self.parent.parent.__class__(value, context=self.context)
        return serializer.data

class UserSkillSerializer(serializers.ModelSerializer):
    sub_skills = RecursiveField(many=True, read_only=True)  # Handle sub-skills recursively

    class Meta:
        model = UserSkill
        fields = ['id', 'name', 'sub_skills']  # 'name' should correspond to the field in your UserSkill model

    def to_representation(self, instance):
        # Ensure that 'instance' is not a QuerySet but an individual object
        representation = super().to_representation(instance)
        return {
            instance.name: representation['sub_skills'] if representation['sub_skills'] else instance.name
        }