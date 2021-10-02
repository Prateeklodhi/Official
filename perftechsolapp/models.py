from typing import Tuple
from django.db import models
from django.db.models.fields import CharField, EmailField
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.
class Client(models.Model):
    name = models.CharField(max_length=150, null= True)
    phone = PhoneNumberField(null = True, blank = True, unique = True)
    email = models.EmailField(null = True, max_length=200)
    services =(
        ('None','Select Type Of Service'),
        ('Android Apps','Android Apps'),
        ('Website Development','Website Development'),
        ('Networking','Networking')
    ) 
    service = models.CharField(max_length=100,null= True,choices= services,default=" ")
    project_dec = models.CharField(max_length=400, null= True)
    message = models.CharField(max_length=300, null= True)
    
    