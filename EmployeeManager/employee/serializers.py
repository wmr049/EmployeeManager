from rest_framework import serializers
from .models import Employee

class EmployeeSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Employee
        fields = '__all__'

    def create(self, validated_data):
        return Employee.objects.create(**validated_data)
        
    def update(self, validated_data):
        instance.title = validated_data.get('name', instance.name)
        instance.save()
        return instance