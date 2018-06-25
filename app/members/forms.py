from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class SignupForm(forms.Form):
    username = forms.CharField(
        label='Your ID',
        max_length=50
    )
    name = forms.CharField(
        label='Your Name',
        max_length=40
    )
    password = forms.CharField(
        widget=forms.PasswordInput(),
        label='password'
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(),
        label='Again password'
    )
    email = forms.EmailField(
        label='Your Email',
        max_length=100
    )
    # password = forms.CharField(type=password, label='Your Password')
    # password2 = forms.PasswordInput()

    def clean_username(self):
        if User.objects.filter(username=self.cleaned_data['username']).exists():
            raise ValidationError('중복된 아이디다')
