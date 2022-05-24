from django.db import models
from khachhang.models import MyUser
from phong.models import Phong
from django.utils import timezone
# Create your models here.
class ChiTietBooking(models.Model):
    mabooking= models.AutoField(primary_key=True)
    tendn= models.ForeignKey(MyUser, on_delete=models.CASCADE)
    sophong= models.ForeignKey(Phong, on_delete=models.CASCADE,default=0)
    ngaynhanphong= models.DateTimeField(default= timezone.now)
    ngaytratphong= models.DateTimeField(default= timezone.now)
    thanhtien=models.BigIntegerField(default=0)
