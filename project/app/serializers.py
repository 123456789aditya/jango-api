from .models import Student
from rest_framework import serializers

class StudentSerializer(serializers.Serializer):
    name=serializers.CharField()
    rollno=serializers.IntegerField()
    city=serializers.CharField()
    
    