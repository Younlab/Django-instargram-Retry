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


        if password == password2:
            User.objects.create_user(username=username, password=password2, email=email, last_name=last_name,)
            user = authenticate(request, username=username, password=password2,)
            login(request, user)
            return redirect('posts:post-list')
        else:
            return HttpResponse('비밀번호가 일치하지 않습니다.')
    else:
        return render(request, 'members/signup.html')
