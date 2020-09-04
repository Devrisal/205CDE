from django.db import models
from  datetime import datetime, date
# Create your models here.
#model for registration
class Usermodel(models. Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200 )
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=200)
    username = models.CharField(max_length=20 )
    password = models.CharField(max_length=20)

    def __str__(self):
        return self.first_name


#event models     
class AddEvent(models. Model):
    id = models.AutoField(primary_key=True)
    event_name=models.CharField(max_length=100)
    location=models.CharField(max_length=100)
    description=models.CharField(max_length=200)
    event_date=models.DateTimeField(default=datetime.now, blank=True) 
 


#packages models
class AddPackage(models.Model):
    id = models.AutoField(primary_key=True)
    package_name=models.CharField(max_length=100)
    duration=models.CharField(max_length=100)
    price=models.CharField(max_length=200)
 