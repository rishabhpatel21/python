from django.shortcuts import render
from django.http import HttpResponse

def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def contact(request):
  return HttpResponse("<h1>Welcome to Chai's Django Project: Contact page</h1>")