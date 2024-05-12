from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
  return HttpResponse('<h1>Good Bye</h1>')

def user_page(request, user_name):
  return HttpResponse('<h1>{}\'s page</h1>'.format(user_name))

def number_page(request, user_name, number):
  user_name = user_name.upper()
  return HttpResponse('<h1>{}\'s page , number = {}</h1>'.format(user_name, number))