from django.db import models
from django.utils.safestring import mark_safe
# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=70)
    email = models.EmailField(max_length=100, null=True)
    image = models.ImageField(upload_to='media', blank=True, null=True)

    def __str__(self):
        return self.name
    
    
    