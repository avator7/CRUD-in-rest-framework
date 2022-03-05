from rest_framework import serializers
from management.models import *


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'





class Student_detailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student_detail
        fields = ['marks', 'Parent_name', 'Address']