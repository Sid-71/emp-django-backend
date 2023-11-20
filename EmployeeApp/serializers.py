from rest_framework import serializers
from EmployeeApp.models import Employees,Departments



class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Departments
        fields = '__all__'


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Employees
        fields = '__all__'
        # fields = ('EmployeeId','EmployeeName','Department','DateOfJoining','isAdmin','email')
