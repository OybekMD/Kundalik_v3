from rest_framework import serializers
from .models import SchoolModel, SchoolClassModel, TeacherModel, StudentModel
from django.shortcuts import get_object_or_404

    
class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = SchoolModel
        fields = '__all__'

class SchoolClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = SchoolClassModel
        fields = '__all__'
    
class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeacherModel
        fields = '__all__'

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentModel
        fields = '__all__'

     
            