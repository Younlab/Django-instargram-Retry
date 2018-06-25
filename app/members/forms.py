from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class SignupForm(forms.Form):
    username = forms.CharField(
        label='Your ID',
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
            }
        )
    )
    name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
            }
        ),
        label='Your Name',
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class':'form-control',
            }
        ),
        label='password',
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
            }
        ),
        label='Again password'
    )
    email = forms.EmailField(
        label='Your Email',
        widget=forms.TextInput(
            attrs={
                'class':'form-control'
            }
        )
    )

    def clean_username(self):
        data = self.cleaned_data['username']
        on_data = User.objects.filter(username=data)
        if on_data.exists():
            print('중복된 값이다.')
            raise forms.ValidationError('중복된 아이디다')
        print('no')
        return data
