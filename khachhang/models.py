from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class MyUser(AbstractUser):
    tendn = AbstractUser.username
    sdt=models.CharField(default='',max_length=11)
    
    