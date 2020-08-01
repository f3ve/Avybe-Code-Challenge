from django.urls import path
from django.contrib.auth.views import LoginView
from . import views

appname='accounts'
urlpatterns = [
  path('', views.indexView, name='home'),
  path('login/', LoginView.as_view(), name='login_url'),
  path('register/', views.registerView, name='register_url'),
]
  # path('profile/', views.profileView, name='profile'),
  # path('logout/', views.logutView, name='register')
  # path('login/', views.loginView, name='login'),