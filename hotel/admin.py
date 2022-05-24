from django.contrib import admin
from khachhang.models import MyUser
from phong.models import Phong
from chitietbooking.models import ChiTietBooking
# Register your models here.
admin.site.register(MyUser)
admin.site.register(Phong)
admin.site.register(ChiTietBooking)

