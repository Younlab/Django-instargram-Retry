from django.urls import path
from . import views

app_name = 'posts'
urlpatterns = [
    path('', views.post_list, name='post-list'),
    path('postedit/', views.post_create, name= 'post-edit'),
    path('<int:pk>/', views.post_detail, name='post-detail'),

]