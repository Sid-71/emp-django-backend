from django.db import models
from django.core.validators import RegexValidator
# Create your models here.


class Departments(models.Model):
    DepartmentId = models.AutoField(primary_key=True)
    DeprartmentName = models.CharField(max_length=100)


class Employees(models.Model):
    EmployeeId = models.AutoField(primary_key=True)
    EmployeeName = models.CharField(max_length=30)
    Department = models.CharField(max_length=100)
    # DateOfJoining = models.DateField()
    isAdmin = models.BooleanField(default=False)
    email = models.CharField(max_length=100,unique=True)
    
    # Password should be at least 8 characters long and contain at least one digit and one symbo
    password = models.CharField(max_length=50)





    
    

