from django.contrib.auth import authenticate, login, logout, get_user_model
from django.http import HttpResponse
from django.shortcuts import render, redirect

# User 클래스 자체를 가져올때는 get_user_model()
# ForeignKey에 User 모델을 지정할때는 settings.AUTH_USER_MODEL
from .forms import SignupForm

User = get_user_model()

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password,)
        if user is not None:
            login(request, user)
            return redirect('posts:post-list')
        else:
            return redirect('members:login')
    else:
        return render(request, 'members/login.html')

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('posts:post-list')
    else:
        return redirect('posts:post-list')


def sign_up(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            # 유효할 경우 유저 생성 및 redirect
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            password2 = form.cleaned_data['password2']
            email = form.cleaned_data['email']
            name = form.cleaned_data['name']
            user = User.objects.create_user(username=username, password=password, last_name=name, email=email)
            login(request, user)
            return redirect('posts:post-list')
        else:
            result = '\n'.join(['{}: {}'.format(key, value) for key, value in form.errors.items()])
            return HttpResponse(result)
    else:
        form = SignupForm()
        context = {
            'form':form,
        }
        return render(request, 'members/signup.html', context)





    #     # if not username:
    #     #     context['errors'].append('username 를 입력해주세요')
    #     #
    #     # if not email:
    #     #     context['errors'].append('email를 입력해주세요')
    #     #
    #     # if not password:
    #     #     context['errors'].append('password를 입력해주세요')
    #     #
    #     # if not password2:
    #     #     context['errors'].append('password 확인 검사를 입력해주세요')
    #
    #     required_field = {
    #         'username':{
    #             'verbose_name':'아이디',
    #         },
    #         'email':{
    #             'verbose_name':'이메일',
    #         },
    #         'password':{
    #             'verbose_name': '비밀번호',
    #         },
    #         'password2':{
    #             'verbose_name': '비밀번호 확인',
    #         },
    #     }
    #     # for field_name in required_field:
    #         # if not locals()[field_name]:
    #             # context['errors'].append(f'{required_field[field_name]['verbose_name']}을(를) 채워주세요')
    #
    #
    #     if not context['errors']:
    #
    #         user = User.objects.create_user(username=username, password=password2, email=email, last_name=last_name,)
    #         login(request, user)
    #         return redirect('posts:post-list')
    #
    # return render(request, 'members/signup.html', context)
