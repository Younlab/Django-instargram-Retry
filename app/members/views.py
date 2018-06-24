from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect


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
        username = request.POST['username']
        last_name = request.POST['last_name']
        password = request.POST['password']
        password2 = request.POST['password2']
        email = request.POST['email']

        # 비밀번호 확인하기
        if password == password2:
            # 일치할 경우에 계정 생성
            User.objects.create_user(username=username, password=password2, email=email, last_name=last_name,)
            # 생성후 바로 로그인 처리하기
            user = authenticate(request, username=username, password=password2,)
            # 로그인
            login(request, user)
            # defult page 로 이동
            return redirect('posts:post-list')
        else:
            # 비밀번호 확인이 일치하지 않을 경우에 메세지 리턴,
            return HttpResponse('비밀번호가 일치하지 않습니다.')
    else:
        # signup 템플릿 불러오기
        # 일단 POST 로 request 가 오지 않았기 때문에 우선 실행하여 else 문에 넣었다.
        return render(request, 'members/signup.html')
