from rest_framework import serializers
from user_authentication.models import User,UserProfile
from django.contrib.auth.hashers import check_password,make_password
from django.db import transaction

class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'password']

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        if password:
            '''
            Hashing Password before saving it to database
            '''
            validated_data['password'] = make_password(password)
        try :
            '''
            If anything Fails this task will be reverted
            '''
            with transaction.atomic():
                user = User.objects.create(**validated_data)
                '''
                Creating Profile Instance while creating User Instance
                '''
                UserProfile.objects.create(user=user)
                return user
        except Exception as e:
            raise serializers.ValidationError({"detail": str(e)})


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','email','fullname']