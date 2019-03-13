from django import forms
from django.forms import ModelForm,TextInput,Select,FileInput
from .models import Post, Good,PostReply
from accounts.models import UserInfo

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
        fields = ('good_name','good_description','plat','price','good_photo','online','lower')

        widgets = {
            'good_name': TextInput(attrs={"class":"form-control"}),
            'good_description': TextInput(attrs={"class":"form-control"}),
            'plat': TextInput(attrs={"class":"form-control",}),
            'price': TextInput(attrs={"class": "form-control"}),
            'online': Select(attrs={"class":""}),
            'lower': Select(attrs={"class":""}),
        }

class PostForm(forms.ModelForm):
    content = forms.CharField(max_length=128,
                              widget=forms.Textarea(attrs={'class': 'comment-input',}))
    class Meta:
        model = Post
        fields = ['message' ]


class ReplyForm(forms.ModelForm):

    class Meta:
        model = PostReply
        fields = ['content']
        widgets = {'content': forms.Textarea(attrs={'rows': 3, 'placeholder': '写下你的回复...'})}


