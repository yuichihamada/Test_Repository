from django.shortcuts import get_object_or_404, redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.base import TemplateView
from django.views.generic.edit import(
  UpdateView, DeleteView, CreateView,FormView
)
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from accounts.models import Users
from . models import (
  WantItems, ToDoThings, AchievedThings
)
from . forms import (
  UserUpdateForm, RegistItemForm, ItemUpdateForm, RegistThingForm,  ThingUpdateForm, ConfirmAchievedItemForm, ConfirmAchievedThingForm
)
from datetime import date, datetime, timedelta
from django.db import transaction
import os


class MyPageView(LoginRequiredMixin, TemplateView):
  template_name = os.path.join('lists', 'my_page.html')
  
  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['user'] = Users.objects.filter(id=self.request.user.id).first()

class UserInformationView(LoginRequiredMixin, DetailView):
  model = Users
  template_name = os.path.join('lists', 'user_information.html')


class UserUpdateView(LoginRequiredMixin, UpdateView):
  model = Users
  form_class = UserUpdateForm
  template_name = os.path.join('lists', 'update_user.html')
  
  def get_success_url(self):
    return reverse_lazy('lists:user_information', kwargs={'pk': self.request.user.id})


class UserDeleteView(LoginRequiredMixin, DeleteView):
  template_name = os.path.join('lists', 'delete_user.html')
  model = Users
  success_url = reverse_lazy('accounts:home')


class WantListView(LoginRequiredMixin, ListView):
  model = WantItems
  template_name = os.path.join('lists', 'want_list.html')
  
  def get_queryset(self):
    query = super().get_queryset()
    user = self.request.user
    query = query.filter(user=user)
    item_name  = self.request.GET.get('item_name', None)
    if item_name:
      query = query.filter(
        name__icontains = item_name
      )
    order_by_date = self.request.GET.get('order_by_date', 0)
    if order_by_date == '1':
      query = query.order_by('target_date')
    if order_by_date == '2':
      query = query.order_by('-target_date')
    time_filter = self.request.GET.get('time_filter', 0)
    if time_filter:
      start_date = datetime.now()
      if time_filter == '1':
        end_date = start_date + timedelta(days=30)
      elif time_filter == '2':
        end_date = start_date + timedelta(days=365)
      elif time_filter == '3':
        end_date = start_date + timedelta(days=3*365)
      elif time_filter == '4':
        end_date = start_date + timedelta(days=10*365)
      else:
        return query
      query = query.filter(target_date__range=[start_date, end_date])
    return query
  
  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['item_name'] = self.request.GET.get('item_name', '')
    order_by_date = self.request.GET.get('order_by_date')
    if order_by_date == '1':
      context['ascending'] = True
    elif order_by_date == '2':
      context['descending'] = True
    time_filter = self.request.GET.get('time_filter')
    if time_filter == '1':
      context['within_month'] = True
    elif time_filter == '2':
      context['within_year'] = True
    elif time_filter == '3':
      context['within_3years'] = True
    elif time_filter == '4':
      context['within_10years'] = True
    elif time_filter == '5':
      context['all_time'] = True
    total_price = 0
    for item in self.object_list:
      total_price += item.price
    context['total_price'] = total_price
    return context


class RegistItemView(LoginRequiredMixin, CreateView):
  template_name = os.path.join('lists', 'regist_item.html')
  form_class = RegistItemForm
  success_url = reverse_lazy('lists:want_list')
  
  def get_form_kwargs(self):
    kwargs = super().get_form_kwargs()
    kwargs['user'] = self.request.user
    return kwargs
  

class ItemDetailView(LoginRequiredMixin, DetailView):
  model = WantItems
  template_name = os.path.join('lists', 'item_detail.html')


class ConfirmAchievedItemView(LoginRequiredMixin, FormView):
  template_name = os.path.join('lists', 'confirm_achieved_item.html')
  form_class = ConfirmAchievedItemForm
  
  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    want_item_pk = self.kwargs['pk']
    context['want_item'] = get_object_or_404(WantItems, pk=want_item_pk)
    return context
  
  def form_valid(self, form):
    want_item_pk = self.kwargs['pk']
    want_item = get_object_or_404(WantItems, pk=want_item_pk)
    price = form.cleaned_data['price']
    achieved_date = form.cleaned_data['achieved_date']
    achieved_thing = AchievedThings(
      name = want_item.name,
      detail = want_item.detail,
      picture = want_item.picture,
      price = price,
      achieved_date = achieved_date,
      text = want_item.reason,
      user = want_item.user,
      type = 'WantItem',
      create_at = datetime.now(),
      update_at = datetime.now(),
    )
    achieved_thing.save()
    want_item.delete()
    return redirect('lists:achieved_list')
    
  
class ItemUpdateView(LoginRequiredMixin, UpdateView):
  model = WantItems
  form_class = ItemUpdateForm
  template_name = os.path.join('lists', 'update_item.html')
  
  def get_success_url(self):
    return reverse_lazy('lists:item_detail', kwargs={'pk': self.object.id})
  

class ItemDeleteView(LoginRequiredMixin, DeleteView):
  model = WantItems
  template_name = os.path.join('lists', 'delete_item.html')
  success_url = reverse_lazy('lists:want_list')


class TodoListView(LoginRequiredMixin, ListView):
  model = ToDoThings
  template_name = os.path.join('lists', 'todo_list.html')
  
  def get_queryset(self):
    query = super().get_queryset()
    user = self.request.user
    query = query.filter(user=user)
    thing_name  = self.request.GET.get('thing_name', None)
    if thing_name:
      query = query.filter(
        name__icontains = thing_name
      )
    order_by_date = self.request.GET.get('order_by_date', 0)
    if order_by_date == '1':
      query = query.order_by('target_date')
    if order_by_date == '2':
      query = query.order_by('-target_date')
    time_filter = self.request.GET.get('time_filter', 0)
    if time_filter:
      start_date = datetime.now()
      if time_filter == '1':
        end_date = start_date + timedelta(days=30)
      elif time_filter == '2':
        end_date = start_date + timedelta(days=365)
      elif time_filter == '3':
        end_date = start_date + timedelta(days=3*365)
      elif time_filter == '4':
        end_date = start_date + timedelta(days=10*365)
      else:
        return query
      query = query.filter(target_date__range=[start_date, end_date])
    return query
  
  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['thing_name'] = self.request.GET.get('thing_name', '')
    order_by_date = self.request.GET.get('order_by_date')
    if order_by_date == '1':
      context['ascending'] = True
    elif order_by_date == '2':
      context['descending'] = True
    time_filter = self.request.GET.get('time_filter')
    if time_filter == '1':
      context['within_month'] = True
    elif time_filter == '2':
      context['within_year'] = True
    elif time_filter == '3':
      context['within_3years'] = True
    elif time_filter == '4':
      context['within_10years'] = True
    elif time_filter == '5':
      context['all_time'] = True
    total_price = 0
    for thing in self.object_list:
      total_price += thing.price
    context['total_price'] = total_price
    return context
  


class RegistThingView(LoginRequiredMixin, CreateView):
  template_name = os.path.join('lists', 'regist_thing.html')
  form_class = RegistThingForm
  success_url = reverse_lazy('lists:todo_list')
  
  def get_form_kwargs(self):
    kwargs = super().get_form_kwargs()
    kwargs['user'] = self.request.user
    return kwargs
  

class ThingDetailView(LoginRequiredMixin, DetailView):
  model = ToDoThings
  template_name = os.path.join('lists', 'thing_detail.html')


class ConfirmAchievedThingView(LoginRequiredMixin, FormView):
  template_name = os.path.join('lists', 'confirm_achieved_thing.html')
  form_class = ConfirmAchievedThingForm
  
  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    todo_thing_pk = self.kwargs['pk']
    context['todo_thing'] = get_object_or_404(ToDoThings, pk=todo_thing_pk)
    return context
  
  def form_valid(self, form):
    todo_thing_pk = self.kwargs['pk']
    todo_thing = get_object_or_404(ToDoThings, pk=todo_thing_pk)
    price = form.cleaned_data['price']
    achieved_date = form.cleaned_data['achieved_date']
    achieved_thing = AchievedThings(
      name = todo_thing.name,
      detail = todo_thing.detail,
      picture = todo_thing.picture,
      price = price,
      achieved_date = achieved_date,
      text = todo_thing.reason,
      user = todo_thing.user,
      type = 'ToDoThing',
      create_at = datetime.now(),
      update_at = datetime.now(),
    )
    achieved_thing.save()
    todo_thing.delete()
    return redirect('lists:achieved_list')


class ThingUpdateView(LoginRequiredMixin, UpdateView):
  model = ToDoThings
  form_class = ThingUpdateForm
  template_name = os.path.join('lists', 'update_thing.html')
  
  def get_success_url(self):
    return reverse_lazy('lists:thing_detail', kwargs={'pk': self.object.id})
  

class ThingDeleteView(LoginRequiredMixin, DeleteView):
  model = ToDoThings
  template_name = os.path.join('lists', 'delete_thing.html')
  success_url = reverse_lazy('lists:todo_list')


class AchievedListView(LoginRequiredMixin, ListView):
  model = AchievedThings
  template_name = os.path.join('lists', 'achieved_list.html')
  
  def get_queryset(self):
    query = super().get_queryset()
    user = self.request.user
    query = query.filter(user=user)
    thing_name  = self.request.GET.get('thing_name', None)
    if thing_name:
      query = query.filter(
        name__icontains = thing_name
      )
    order_by_date = self.request.GET.get('order_by_date', 0)
    if order_by_date == '1':
      query = query.order_by('achieved_date')
    if order_by_date == '2':
      query = query.order_by('-achieved_date')
    type_filter = self.request.GET.get('type_filter', 0)
    if type_filter == '1':
      query = query.filter(type = 'WantItem')
    if type_filter == '2':
      query = query.filter(type = 'ToDoThing')
    return query
  
  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['thing_name'] = self.request.GET.get('thing_name', '')
    order_by_date = self.request.GET.get('order_by_date')
    if order_by_date == '1':
      context['ascending'] = True
    elif order_by_date == '2':
      context['descending'] = True
    type_filter = self.request.GET.get('type_filter')
    if type_filter == '1':
      context['wantitem'] = True
    elif type_filter == '2':
      context['todothing'] = True
    total_price = 0
    for thing in self.object_list:
      total_price += thing.price
    context['total_price'] = total_price
    return context


class AchievedThingDetailView(LoginRequiredMixin, DetailView):
  model = AchievedThings
  template_name = os.path.join('lists', 'achieved_thing_detail.html')


class AchievedThingDeleteView(LoginRequiredMixin, DeleteView):
  model = AchievedThings
  template_name = os.path.join('lists', 'delete_achieved_thing.html')
  success_url = reverse_lazy('lists:achieved_list')


class OverdueListView(LoginRequiredMixin, TemplateView):
  model = AchievedThings
  template_name = os.path.join('lists', 'overdue_list.html')
  
  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    today = date.today()
    context['want_list'] = WantItems.objects.filter(target_date__lt=today)
    context['todo_list'] = ToDoThings.objects.filter(target_date__lt=today)
    return context