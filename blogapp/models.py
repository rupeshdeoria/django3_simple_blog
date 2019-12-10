from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class BlogArtical(models.Model):
    title = models.CharField(max_length=400)
    blogcontent = models.TextField()
    author = models.ForeignKey(User,on_delete=models.DO_NOTHING)

    
