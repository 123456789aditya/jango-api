from django.shortcuts import render
from .models import Student
from django.http import JsonResponse
from .serializers import StudentSerializer
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
import io
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
# def alldata(request):
#     data=Student.objects.all()
#     serialize=StudentSerializer(data,many=True)
#     print(data)
#     print(serialize.data)
#     return JsonResponse(serialize.data,safe=False)

# def singledata(request):
#     data=Student.objects.get(id=1)
#     serialize=StudentSerializer(data)
#     print(serialize)
#     return JsonResponse(serialize.data,safe=False)

@csrf_exempt    
def createdata(request):
    if request.method=="POST":
        json_data=request.body
        stream=io.BytesIO(json_data)
        python_data=JSONParser().parse(stream)
        serializer=StudentSerializer(data=python_data)
        if serializer.is_valid():
            serializer.save()
            msg="Data created successfully"
            json_data=JSONRenderer().render(msg)
            return HttpResponse(json_data,content_type='application/json')
        json_data=JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data,content_type='application/json')
        