
# website/urls.py
from django.urls import path
from . import views

app_name = 'website'

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('charity-projects/', views.charity_projects, name='charity_projects'),
    path('join-us/', views.join_us, name='join_us'),
    path('request-website/', views.request_website, name='request_website'),
    path('contact/', views.contact, name='contact'),
]
