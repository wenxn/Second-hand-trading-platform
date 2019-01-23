from .models import UserInfo
from django.forms import ModelForm,TextInput,Select

class user_form(ModelForm):
    class Meta:
        model = UserInfo
        fields = ('username','password')

        widgets = {
            'username': TextInput(attrs={"class":"form-control"}),
            'password': TextInput(attrs={"class":"form-control",}),
        }