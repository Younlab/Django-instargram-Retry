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
      if User.objects.filter(username=data).exists():
          print('id errors')
          raise ValidationError('중복된 아이디가 존재합니다.')
      else:
          print('pass')
          return data
