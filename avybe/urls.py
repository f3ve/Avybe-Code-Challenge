from django.urls import path

from . import views

appname='avybe'
urlpatterns = [
  path('', views.indexView, name='home'),
  path('register/', views.registerView, name='register'),
]
  # path('profile/', views.profileView, name='profile'),
  # path('logout/', views.logutView, name='register')
  # path('login/', views.loginView, name='login'),