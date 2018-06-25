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

      # data 는 자기 자신, 여기서는 위에 정의한 username 를 가져온다.
      data = self.cleaned_data['username']

      # 만약 User에 등록된 username 가 있을경우 True 반환
      if User.objects.filter(username=data).exists():

          print('id errors')

          # 중복된 username 가 있으면 안되므로 에러 출력
          raise ValidationError('중복된 아이디가 존재합니다.')
      else:

          # 문제되는 것이 없으면 들어온 username 그대로 내보냄
          print('pass')
          return data


    def clean(self):

        # 이것에 개념을 잘 이해하지 못했음
        # 추측으로는 위에 정의한 변수 내부에 CharField 등의 하위클래스에 무조건 clean()이
        # 들어있다고 보고 모든 변수에서 사용된 clean() 변수를 상속, clean()에 들어온 값도 그대로 가져옴
        cleaned_data = super().clean()

        # pass1 clean() 에 들어온 값에서 password 값을 꺼내옴
        pass1 = cleaned_data.get('password')
        pass2 = cleaned_data.get('password2')

        # pass1 과 pass2 의 값이(form으로 들어온 값) 일치하지 않을때
        if pass1 != pass2:

            # 에러메세지 출력, 위에처럼 그대로 안내보내도 되는듯,
            raise ValidationError('패스워드가 동일하지 않습니다.')