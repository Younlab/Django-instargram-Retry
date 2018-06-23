from django.http import HttpResponse
from django.shortcuts import render

def post_list(request):
    return HttpResponse('post-list')


def post_deatil(request, pk):
    return HttpResponse(f'post-detail {pk}')
