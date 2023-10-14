from rest_framework import serializers
from .models import *


class StudentSerializer(serializers.ModelSerializer):
    """ModelSerializer for Students Model"""
    class Meta:
        """StudentSerializer Meta Class"""
        model = Student
        fields = '__all__'

        
    def create(self, validated_data):
        return Student.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.roll_number = validated_data.get('roll_number',instance.roll_number)
        instance.first_name = validated_data.get('roll_number',instance.first_name)
        instance.last_name = validated_data.get('roll_number',instance.last_name)
        instance.dob = validated_data.get('roll_number',instance.dob)
        instance.address = validated_data.get('roll_number',instance.address)
        instance.save()
        return instance


class SubjectSerializer(serializers.ModelSerializer):
    """ModelSerializer for Subjects Model"""
    class Meta:
        """SubjectSerializer Meta Class"""
        model = Subject
        fields = '__all__'


    def create(self, validated_data):
        return Subject.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.subject_name = validated_data.get('subject_name',instance.subject_name)
        instance.save()
        return instance