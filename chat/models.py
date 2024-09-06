from django.db import models

# Create your models here.


class Messages(models.Model):
    sender = models.CharField(max_length=20,blank=False)
    text = models.CharField(max_length=200,blank=False)
    reciever = models.CharField(max_length=20,blank=False)

    