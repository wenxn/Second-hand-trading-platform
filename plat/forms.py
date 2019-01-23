from django import forms
from django.forms import ModelForm,TextInput,Select,CheckboxInput
from .models import Post, Good

'''
class NewPlatForm(forms.ModelForm):
    message = forms.CharField(
        widget=forms.Textarea(
            attrs={'rows': 5, 'placeholder': 'What is in your mind?'}
        ),
        max_length=4000,
        help_text='The max length of the text is 4000.'
    )

    class Meta:
        model = Goods
        fields = ['subject', 'message']

'''

class goods_form(ModelForm):
    class Meta:
        model = Good
        fields = ('good_name','good_description','plat','price','online','lower')

        widgets = {
            'good_name': TextInput(attrs={"class":"form-control"}),
            'good_description': TextInput(attrs={"class":"form-control"}),
            'plat': TextInput(attrs={"class":"form-control",}),
            'price': TextInput(attrs={"class": "form-control"}),
            'online': Select(attrs={"class":"custom-control-input"}),
            'lower': Select(attrs={"class":"custom-control-input"}),
        }

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['message', ]