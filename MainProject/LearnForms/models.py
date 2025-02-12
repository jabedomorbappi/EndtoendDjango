from django.db import models

# Create your models here.

class Contact(models.Model):
    name=models.CharField(max_length=20)
    phone=models.CharField(max_length=20)
    content=models.CharField(max_length=10)
    
    
    def __str__(self):
        return self.name  
    
class AnotherModels(models.Model):
    fname=models.CharField(max_length=20)
    lname=models.CharField(max_length=20)
    roll=models.IntegerField()
    address=models.CharField(max_length=20)
    district=models.CharField(max_length=20)
    country=models.CharField(max_length=20)
    
    def __str__(self):
        return f"{self.fname} {self.lname} - Roll: {self.roll}"
        