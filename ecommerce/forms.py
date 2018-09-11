from django import forms
from django.http import HttpResponse
from .models import post
from django.contrib.auth import authenticate

class LoginForm(forms.Form):
    Userid = forms.CharField( max_length=50 )
    Password = forms.CharField( widget=forms.PasswordInput(attrs=dict(required=True)))

    def clean(self):
        user = self.cleaned_data['Userid']
        passwd = self.cleaned_data['Password']
        valid = authenticate(username=user,password = passwd)
        if not valid:
            raise forms.ValidationError("Invalid pls check it")
        return self.cleaned_data

class PostForm(forms.ModelForm):
    class Meta:
        model = post
        fields = ["user","title","content"]
