from django import forms
from django.contrib.auth import get_user_model

from django.core.exceptions import ValidationError

User = get_user_model()

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
    # username field의 clean()실행 결과가 self.cleaned_data['username']에 있음
      # data 는 자기 자신, 여기서는 위에 정의한 username 를 가져온다.
      data = self.cleaned_data['username']

      # 만약 User에 등록된 username 가 있을경우 True 반환
      if User.objects.filter(username=data).exists():

          print('id errors')

          # 중복된 username 가 있으면 안되므로 에러 출력
          raise ValidationError('중복된 아이디가 존재합니다.')
      else:
          # 문제되는 것이 없으면 들어온 username 그대로 내보냄
          return data


    def clean(self):

        # 이것에 개념을 잘 이해하지 못했음
        # 추측으로는 위에 정의한 변수(username 등등..) 내부에 CharField 등의 하위클래스에 무조건 clean()이
        # 들어있다고 보고 모든 변수에서 사용된 clean() 변수를 상속, clean()에 들어온 값도 그대로 가져옴
        super().clean()
        # pass1 clean() 에 들어온 값에서 password 값을 꺼내옴
        pass1 = self.cleaned_data['password']
        pass2 = self.cleaned_data['password2']

        # pass1 과 pass2 의 값이(form으로 들어온 값) 일치하지 않을때
        if pass1 != pass2:

            # 에러메세지 출력, 위에처럼 그대로 안내보내도 되는듯,
            # raise ValidationError('패스워드가 동일하지 않습니다.')
            self.add_error('password2','패스워드가 일치하지 않습니다.')

        return self.cleaned_data
    # def clean_password2(self):
    #     pass1 = self.cleaned_data['password']
    #     pass2 = self.cleaned_data['password2']
    #
    #     if pass1 != pass2:
    #         raise ValidationError('패스워드가 일치하지 않습니다.')
    #     else:
    #         return pass2

    def signup(self):
        username = self.cleaned_data['username']
        email = self.cleaned_data['email']
        password2 = self.cleaned_data['password2']

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password2,
        )
        print(user)
        return user