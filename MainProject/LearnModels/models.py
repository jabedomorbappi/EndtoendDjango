from django.db import models

# Create your models here.

class Employee(models.Model):
    fname=models.CharField(max_length=20)
    lname=models.CharField(max_length=20)
    mob=models.CharField(max_length=10)
    job=models.CharField(max_length=20)
    
    def __str__(self):
        return self.fname   
    
class Students(models.Model):
    fname=models.CharField(max_length=20)
    lname=models.CharField(max_length=20)
    mob=models.CharField(max_length=10)
    job=models.CharField(max_length=20)
    
    def __str__(self):
        return self.fname    
