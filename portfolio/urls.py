from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('articles/', views.articles, name='articles'),
    path('projects/', views.projects, name='projects'),
    path('contactme/', views.contact_me, name='contact_me'),
]
