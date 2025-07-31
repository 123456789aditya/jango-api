# from .models import Student
from rest_framework import serializers
from .models import Student


# class StudentSerializer(serializers.Serializer):
#     name=serializers.CharField()
#     rollno=serializers.IntegerField()
#     city=serializers.CharField()
    
    
#     def create(self, validated_data):
#         return Student.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         instance.name = validated_data.get('name', instance.name)
#         instance.rollno = validated_data.get('rollno', instance.rollno)
#         instance.city = validated_data.get('city', instance.city)
#         instance.save()
#         return instance
    
# class StudentSerializer(serializers.ModelSerializer):
#     class Meta:
#         model=Student
#         fields='__all__'