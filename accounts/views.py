from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView
from django import forms
from .models import Profile
from django.urls import reverse_lazy, reverse

def indexView(request):
  return render(request, 'accounts/index.html')

@login_required
def profileView(request):
  currentUser = request.user
  try:
    p = Profile.objects.get(user=currentUser)
  except (Profile.DoesNotExist):
    return redirect(reverse('createProfile'))
  else: 
    return render(request, 'accounts/profile.html', {'p':p})

def registerView(request):
  if request.method == "POST":
    form = UserCreationForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('login_url')
  else:
    form = UserCreationForm()

  return render(request, 'registration/register.html', {'form':form})

class CreateProfile(LoginRequiredMixin, CreateView):
  model = Profile
  fields = ['image', 'nickname']
  success_url = reverse_lazy('profile')

  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)

class UpdateProfile(LoginRequiredMixin, UpdateView):
  model = Profile
  fields = ['image', 'nickname']
  success_url = reverse_lazy('profile')
  template_name = 'accounts/update-profile.html'