from django.db import models

# Create your models here.
class UserContactData(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=60, default="")
    email = models.CharField(max_length=60, default="")
    phone = models.CharField(max_length=12, default=None)
    address = models.TextField(default="")
    message = models.TextField(default="")