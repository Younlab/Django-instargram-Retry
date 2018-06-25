from django.contrib.auth import authenticate, login, logout, get_user_model
from django.http import HttpResponse
from django.shortcuts import render, redirect

# User 클래스 자체를 가져올때는 get_user_model()
# ForeignKey에 User 모델을 지정할때는 settings.AUTH_USER_MODEL
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
    context = {
        'errors': [],
    }
    if request.method == 'POST':
        username = request.POST['username']
        last_name = request.POST['last_name']
        password = request.POST['password']
        password2 = request.POST['password2']
        email = request.POST['email']

        context['username']=username
        context['email']=email
        # exists를 사용해서 유저가 이미 존재하면 signup으로 다시 redirect
        # 존재하지 않는 경우에만 아래 로직 실행
        # 일치할 경우에 계정 생성

        if User.objects.all().filter(username=username).exists():
            # 단순 redirect 가 아니라, render를 사용
            # render 에 context를 전달
            # errors list에 '유저가 이미 존재함'
            # 템플릿에서는 전달받은 errors를 순회하며 에러메세지를 출력

            context['username'].append(username)
            context['email'].append(email)
            context['errors'].append('유저가 이미 존재합니다.')

        # 비밀번호 확인하기
        if password != password2:
            context['errors'].append('비밀번호가 일치하지 않습니다.')

        if not context['errors']:

            user = User.objects.create_user(username=username, password=password2, email=email, last_name=last_name,)
            login(request, user)
            return redirect('posts:post-list')

    return render(request, 'members/signup.html', context)
