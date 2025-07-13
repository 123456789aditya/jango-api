from .models import Student
from rest_framework import serializers

class StudentSerializer(serializers.Serializer):
    name=serializers.CharField()
    rollno=serializers.IntegerField()
    city=serializers.CharField()
    
    
    def create(self, validated_data):
        return Student.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.roll = validated_data.get('roll', instance.email)
        instance.city = validated_data.get('city', instance.city)
        instance.save()
        return instance
    
    # adhsufcvkmbascdzbh.k