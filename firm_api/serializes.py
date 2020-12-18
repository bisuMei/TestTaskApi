from rest_framework import serializers


class EmployeeSerializer(serializers.Serializer):
    user = serializers.CharField
    first_name = serializers.CharField(max_length=15)
    middle_name = serializers.CharField(max_length=15)
    last_name = serializers.CharField(max_length=15)
    position = serializers.CharField()
    employment_date = serializers.DateField()
    salary = serializers.CharField()
    total_salary_paid = serializers.CharField()
    boss_id = serializers.CharField()
    hierarchy_level = serializers.CharField()