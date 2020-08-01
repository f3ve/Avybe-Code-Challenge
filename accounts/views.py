from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

def indexView(request):
  return render(request, 'accounts/index.html')

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
