from django.urls import path

from . import views

urlpatters = [
  path('', views.indexView, name='home'),
  path('profile/', views.profileView, name='profile'),
  path('login/', views.loginView, name='login'),
  path('register/', views.registerView, name='register'),
  path('logout/', views.logutView, name='register')
]