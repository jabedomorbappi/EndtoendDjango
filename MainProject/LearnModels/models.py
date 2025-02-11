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




# now i want to create a models where i ensure unique rolll 




class Unique_Student(models.Model):
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    roll_number = models.IntegerField(unique=True)  # Unique constraint
    email = models.EmailField(unique=True)  # Also ensuring unique email
    phone = models.CharField(max_length=15)
    course = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.fname} {self.lname} - Roll: {self.roll_number}"
