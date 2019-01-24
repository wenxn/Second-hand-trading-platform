from .models import UserInfo
from django.forms import ModelForm,TextInput,Select,PasswordInput
from django.contrib.auth.models import User

class user_form(ModelForm):
    class Meta:
        model = User
        fields = ('username','password')

        widgets = {
            'username': TextInput(attrs={"class":"form-control"}),
            'password': PasswordInput(attrs={"class":"form-control"}),
        }

class user_detail_form(ModelForm):
    class Meta:
        model = UserInfo
        fields = ('Institute','student_id','email','introduce','photo')

        widgets = {
            'Institute': TextInput(attrs={"class": "form-control"}),
            'student_id': TextInput(attrs={"class": "form-control"}),
            'email': TextInput(attrs={"class": "form-control"}),
            'introduce': TextInput(attrs={"class": "form-control"}),
        }