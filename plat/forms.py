from django import forms
from django.forms import ModelForm,TextInput
from .models import Post, Goods

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
        model = Goods
        fields = ('name','description','plat','price','online')

        widgets = {
            'name': TextInput(attrs={"class":"special"}),
            'description': TextInput(attrs={"class":"form-control"}),
            'plat': TextInput(attrs={"class":"special",}),
            'price': TextInput(attrs={"class": "form-control"}),
        }

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['message', ]