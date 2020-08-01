from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView, UpdateView
from django import forms
from .models import Profile
from django.urls import reverse_lazy

def indexView(request):
  return render(request, 'accounts/index.html')

@login_required
def profileView(request):
  return render(request, 'accounts/profile.html')

def registerView(request):
  if request.method == "POST":
    form = UserCreationForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('login_url')
  else:
    form = UserCreationForm()

  return render(request, 'registration/register.html', {'form':form})

class PostForm(forms.ModelForm):
  class Meta:
    model = Profile
    fields = ['user', 'nickname', 'image']

class CreateProfile(CreateView):
  model = Profile
  form_class = PostForm
  template_name = 'accounts/profile_form.html'
  success_url = reverse_lazy('profile')