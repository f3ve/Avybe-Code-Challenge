from django.shortcuts import render

def indexView(request):
  return render(request, 'index.html')

def profileView(request):
  return render(request, 'profile.html')

def registerView(request):
  return render(request, 'registration/register.html')

