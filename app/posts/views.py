from django.shortcuts import render, redirect

from posts import forms
from .models import Post
from .forms import PostForm


def post_list(request):
    posts = Post.objects.all()
    context = {
        'posts':posts,
    }
    return render(request, 'posts/posts_list.html', context)


def post_detail(request, pk):
    post = Post.objects.get(pk=pk)
    context = {
        'post':post,
    }
    return render(request, 'posts/posts_detail.html', context)

def post_create(request):
    # 새 포스트 만들기
    # 만든 후에는 해당하는 post_detail로 이동
    # forms.py에 PostForm을 구현해서 사용

    # bound form
    # PostForm(request.POST)
    # PostForm(request.POST, request.FILES)

    # POST method 에서는 생성후 redirect
    # GET method에서는 form이 보이는 템플릿 렌더링
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.post_edit()
            form.post_edit().save()
            return redirect('index')

    else:
        form = PostForm()
        context = {
            'form':form
        }
        return render(request, 'posts/post_edit.html', context)


# def post_create(request):
#     # title
#     # text
#     # title = Post.objects.create(title=)
#     # text = Post.objects.create(text=)
#     context = {
#
#     }
#     print(request.POST.get('title'))
#     print(request.POST.get('content'))
#     if request.method == 'POST':
#         # request의 method 값이 'POST' 일 경우
#         # request.POST에 있는 title, text 값과
#         # request.user 에 있는 User 인스턴스 속성을 사용해서
#         # 세 post 인스턴스를 생성
#         # HttpResponse를 사용해 새로생성된 인스턴스의 id, title, text 정보를 출력
#         post = Post.objects.create(
#             author=request.user,
#             title=request.POST['title'],
#             text=request.POST['content'],
#
#         )
#         # HTTP Redirection을 보낼 URL
#         # http://localhost:8000/
#         return redirect('post-list')
#     else:
#         return render(request, 'blog/post_create.html', context)