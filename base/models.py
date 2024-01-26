from django.db import models
from django.db.models.functions import Random
from django.contrib.auth.models import User

# Create your models here.


class Room(models.Model):
    category = models.CharField(null=True,max_length=50,default='')
    host = models.ForeignKey(User, on_delete=models.SET_NULL,null=True)
    #topic
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    location = models.CharField(null=True, max_length=200,default='')
    city = models.CharField(null=True, max_length=200)
    # image = models.ImageField(upload_to='image')
    state = models.CharField(null=True, max_length=200)
    
    #keywords
    contact = models.TextField(null=False)  
    updated = models.DateTimeField(auto_now=True)   #saves time when model is updated
    created = models.DateTimeField(auto_now_add=True) #saves time when model is created (only one time)

    class Meta:
        ordering = [Random()]

    def __str__(self):
        return self.title