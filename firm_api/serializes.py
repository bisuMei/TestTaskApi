from rest_framework import serializers
from django.contrib.auth.models import User


# User Serializer
from firm_api.models import Employee


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email')


# Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])

        return user


class EmployeeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Employee
        fields = ('first_name', 'middle_name', 'last_name',
                  'position', 'employment_date', 'salary', 'total_salary_paid',
                  'boss_id', 'hierarchy_level')

