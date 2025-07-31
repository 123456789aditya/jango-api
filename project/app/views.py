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
#     # print(data)
#     #print(serialize.data)
#     return JsonResponse(serialize.data,safe=False)

# def singledata(request):
#     data=Student.objects.get(id=1)
#     serialize=StudentSerializer(data)
#     print(serialize)
#     return JsonResponse(serialize.data,safe=False)

# @csrf_exempt    
# def createdata(request):
#     if request.method=="POST":
#         json_data=request.body
#         stream=io.BytesIO(json_data)
#         python_data=JSONParser().parse(stream)
#         serializer=StudentSerializer(data=python_data)
#         if serializer.is_valid():
#             serializer.save()
#             msg="Data created successfully"
#             json_data=JSONRenderer().render(msg)
#             return HttpResponse(json_data,content_type='application/json')
#         json_data=JSONRenderer().render(serializer.errors)
#         return HttpResponse(json_data,content_type='application/json')


        
# @csrf_exempt
# def createdata(request,pk):
#     if request.method=="PATCH":
#         json_data=request.body
#         stream=io.BytesIO(json_data)
#         py_new_data=JSONParser().parse(stream)
#         old_data=Student.objects.get(id=pk)
#         x=StudentSerializer(old_data,data=py_new_data,partial =True)
#         if x.is_valid():
#             x.save()
#             y="edit completed"
#             return HttpResponse(y,content_type='application/json')
#         json_data=JSONRenderer().render(x.errors)
#         return HttpResponse(json_data,content_type='application/json')


# @csrf_exempt
# def createdata(request,pk):
#     if request.method=="PUT":
#         json_data=request.body
#         stream=io.BytesIO(json_data)
#         py_new_data=JSONParser().parse(stream)
#         old_data=Student.objects.get(id=pk)
#         x=StudentSerializer(old_data,data=py_new_data)
#         if x.is_valid():
#             x.save()
#             y="edit completed"
#             return HttpResponse(y,content_type='application/json')
#         json_data=JSONRenderer().render(x.errors)
#         return HttpResponse(json_data,content_type='application/json')

# @csrf_exempt
# def deletedata(request,pk):
#     if request.method=="DELETE":
#         json_data=request.body
#         stream=io.BytesIO(json_data)
#         old_data=Student.objects.get(id=pk)
#         old_data.delete()
#         msg="data deleted"
#         json_data=JSONRenderer().render(msg)
#         return HttpResponse(json_data,content_type="application/json")

@csrf_exempt        
def student_api(request):
    if request.method=="GET":
          json_data=request.body
          if json_data:
            stream=io.BytesIO(json_data)
            python_data=JSONParser().parse(stream)
            x=python_data['id']
            data=Student.objects.filter(id=x)
            if data:
               data = Student.objects.get(id=x)
               data1=StudentSerializer(data)
               return JsonResponse(data1.data)
            else:
               msg={'msg':"id dosent exist"}
               return JsonResponse(msg)
          else:
            stu_all=Student.objects.all()
            data1=StudentSerializer(stu_all,many=True)
            return JsonResponse(data1.data,safe=False)
    elif request.method=="POST":
        json_data=request.body
        stream=io.BytesIO(json_data)
        python_data=JSONParser().parse(stream)
        data1=StudentSerializer(data=python_data)
        if data1.is_valid():
            data1.save()
            msg="Data created successfully"
            json_data=JSONRenderer().render(msg)
            return HttpResponse(json_data,content_type='application/json')

        json_data=JSONRenderer().render(data1.errors)
        return HttpResponse(json_data,content_type='application/json')
    elif request.method=="DELETE":
        json_data=request.body
        if json_data:
          pass 
        else:
          message={"msg":"idrequired"}
          return JsonResponse(message)
      
      
      
            
    
    
        