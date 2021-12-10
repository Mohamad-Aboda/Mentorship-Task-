from django.db import models
from rest_framework import serializers
from rest_framework.utils import field_mapping
from .models import Task 



class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task 
        fields = '__all__'

        