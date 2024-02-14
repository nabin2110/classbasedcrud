from django.db import models
from django.urls import reverse


class Blog(models.Model):
    title=models.CharField(max_length=100)
    description=models.TextField()
    image=models.ImageField(upload_to='blogs/',blank=True,null=True)
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('blogs.list')
    
# Create your models here.
