from django import forms
from phong.models import Phong
from chitietbooking.models import ChiTietBooking
from khachhang.models import MyUser
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
class formPhong(ModelForm):
    class Meta:
        model=Phong
        fields=['sophong','loaiphong','gia']
        labels= {'sophong':'So Phong'}
class formPhong(ModelForm):
    class Meta:
        model=Phong
        fields=['sophong','loaiphong','gia']
        labels= {'sophong':'So Phong'}
class SignUpForm(UserCreationForm):
#     first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
#     last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
#     email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    class Meta:
        model = MyUser
        fields = ('username', 'password1','password2','email','sdt')
class formCTBK(ModelForm):
    class Meta:
        model=ChiTietBooking
        fields=['mabooking','tendn','sophong']
        labels= {'sophong':'So Phong'}
        
        
        
        