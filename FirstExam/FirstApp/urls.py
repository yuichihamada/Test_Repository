from django.urls import path
from . import views

app_name = 'FirstApp'

urlpatterns = [
  path('add/<int:num1>/<int:num2>', views.add_page, name='add_page'),
  path('minus/<int:num1>/<int:num2>', views.minus_page, name='minus page'),
  path('div/<int:num1>/<int:num2>', views.div_page, name='div page')
]