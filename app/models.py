from django.db import models

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    mobile_number = models.CharField(max_length=15)
    subject = models.CharField(max_length=200)
    message = models.TextField()

    def __str__(self):
        return self.name
