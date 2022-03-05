from ast import Return
import imp
from urllib import response
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.contrib.auth.models import User

from management.models import *
from management.api.Serializers import *


@api_view(['GET'])
def get_detail_student(request, id):
    try:
        student = Student.objects.get(student_id = id)
    except Student.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = StudentSerializer(student)
        return Response(serializer.data)

@api_view(['GET'])
def get_all_detail_student(request):
    try:
        student = Student.objects.all()
    except Student.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = StudentSerializer(student, many=True)
        return Response(serializer.data)


@api_view(['PUT'])
def get_update_student(request, id):
    try:
        student = Student.objects.get(student_id = id)
    except Student.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "PUT":
        serializer = StudentSerializer(student, data=request.data)
        data = {}
        if serializer.is_valid():
            serializer.save()
            data['success'] = "update successful"
            return response(data=data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




@api_view(['DELETE'])
def get_delete_student(request, id):
    try:
        student = Student.objects.get(student_id = id)
    except Student.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "DELETE":
        operation = student.delete()
        data = {}
        if operation:
            data['success'] = "delete successful"
        else:
            data['failure'] = "delete failed"
        return Response(data=data)




@api_view(['POST'])
def creat_student(request):
    # account = User.objects.get(pk=1)
    # student = Student(student_id = account)
    if request.method == "POST":
        serializer = StudentSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)        





#status.