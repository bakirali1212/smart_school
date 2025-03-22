from rest_framework import serializers
from .models import User, Student, Grade, Homework, BonusPoint

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'first_name', 'last_name', 'role', 'sinf')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(
            username=validated_data['username'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            role=validated_data['role'],
            sinf=validated_data.get('sinf', None)
        )
        user.set_password(validated_data['password'])
        user.save()
        if user.role == 'student':
            Student.objects.create(user=user)
        return user

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

class GradeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grade
        fields = '__all__'

class HomeworkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Homework
        fields = '__all__'

class BonusPointSerializer(serializers.ModelSerializer):
    class Meta:
        model = BonusPoint
        fields = '__all__'
