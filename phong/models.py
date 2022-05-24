from django.db import models

# Create your models here.

class Phong(models.Model):
    choice_phong = {(0,"Standard Room"),(1,"Superior Room"),(2,"Deluxe Room"),(3,"Suite Room")
                    ,(4,"Executive Suite Room"),(5,"President Suite Room"),(6,"Adjacent Rooms"),(7,"Hollywood Twin Room")}
    sophong= models.CharField(max_length=30,primary_key=True,default=0)
    loaiphong = models.IntegerField(choices = choice_phong,default=0)
    gia= models.BigIntegerField(default=0)
    active = models.BooleanField(default = False)
    
    def __str__(self):
        return self.sophong