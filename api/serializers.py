from django.db.models import fields
from rest_framework import serializers
from .models import Student

# class StudentSerializer(serializers.Serializer):
#     id = serializers.IntegerField()
#     name = serializers.CharField(max_length=70)
#     roll = serializers.IntegerField()
#     city = serializers.CharField(max_length=70)

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'