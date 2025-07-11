from django.shortcuts import render
from .models import Student
from django.http import JsonResponse
from .serializers import StudentSerializer
# Create your views here.
# def alldata(request):
#     data=Student.objects.all()
#     serialize=StudentSerializer(data,many=True)
#     print(data)
#     print(serialize.data)
#     return JsonResponse(serialize.data,safe=False)

def singledata(request):
    data=Student.objects.get(id=1)
    serialize=StudentSerializer(data)
    return JsonResponse(serialize.data,safe=False)
    