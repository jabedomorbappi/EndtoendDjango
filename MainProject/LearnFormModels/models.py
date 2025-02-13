from django.db import models

# Create your models here.

class StudentForm(models.Model):
    name = models.CharField(max_length=100)
    roll = models.IntegerField()
    city = models.CharField(max_length=100)
    marks = models.FloatField()
    
    def __str__(self):
        return self.name
