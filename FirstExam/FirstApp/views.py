from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def add_page(request, num1, num2):
  return HttpResponse('<h1>{}</h1>'.format(num1 + num2))

def minus_page(request, num1, num2):
  num1 = float(num1)
  num2 = float(num2)
  return HttpResponse('<h1>{}</h1>'.format(num1 - num2))

def div_page(request, num1, num2):
  num1 = float(num1)
  num2 = float(num2)
  return HttpResponse('<h1>{}</h1>'.format(round(num1 / num2)))