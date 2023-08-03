from django.db import models

# Create your models here.
class tahir(models.model):
  Full Name = model.CharField(max-length=50)
  Email Adress = model.EmailField(max-length=30)
  Mobile Number = model.IntegerField(max-length=12)
  Email Subject = model.CharField(max-length=100)
  Your Message  = model.CharField(max-length=100)

 def __str__(self):
        return self.name
  
  
