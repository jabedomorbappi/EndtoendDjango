from django.db import models
from django.utils.timezone import now

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.TextField(max_length=15)
    def __str__(self):
        return self.name
    
class Post(models.Model):
    Category=(
        ("teacher","Teacher"),
        ("student","Student"),
       
    )
    id=models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    slug=models.CharField(max_length=100,default=title)
    email=models.EmailField(max_length=100)
    salary=models.IntegerField()
    details=models.TextField()
    available=models.BooleanField(default=True)
    category=models.CharField(max_length=100,choices=Category)
    created_at=models.DateTimeField(default=now)
    image=models.ImageField(default="",upload_to="tution/images")
    
    
    
    def __str__(self):
        return self.title    
    

    
