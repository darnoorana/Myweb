

# blog/urls.py
from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.blog_list, name='blog_list'),
    path('create/', views.create_post, name='create_post'),
    path('my-posts/', views.my_posts, name='my_posts'),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
    path('<slug:slug>/edit/', views.edit_post, name='edit_post'),
    path('<slug:slug>/delete/', views.delete_post, name='delete_post'),
]
