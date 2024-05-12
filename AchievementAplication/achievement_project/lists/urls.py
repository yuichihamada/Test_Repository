from django.urls import path
from . views import (
  MyPageView, UserInformationView, UserUpdateView, UserDeleteView, WantListView, RegistItemView, ItemDetailView, ConfirmAchievedItemView, ItemUpdateView, ItemDeleteView,
  TodoListView, RegistThingView, ThingDetailView, ConfirmAchievedThingView, ThingUpdateView, ThingDeleteView, AchievedListView, AchievedThingDetailView, AchievedThingDeleteView, OverdueListView
)

app_name = 'lists'

urlpatterns = [
  path('my_page/', MyPageView.as_view(), name='my_page'),
  path('user_information/<int:pk>', UserInformationView.as_view(), name='user_information'),
  path('update_user/<int:pk>', UserUpdateView.as_view(), name='update_user'),
  path('delete_user/<int:pk>', UserDeleteView.as_view(), name='delete_user'),
  path('want_list/', WantListView.as_view(), name='want_list'),
  path('regist_item/', RegistItemView.as_view(), name='regist_item'),
  path('item_detail/<int:pk>', ItemDetailView.as_view(), name='item_detail'),
  path('confirm_achieved_item/<int:pk>', ConfirmAchievedItemView.as_view(), name='confirm_achieved_item'),
  path('update_item/<int:pk>', ItemUpdateView.as_view(), name='update_item'),
  path('delete_item/<int:pk>', ItemDeleteView.as_view(), name='delete_item'),
  path('todo_list/', TodoListView.as_view(), name='todo_list'),
  path('regist_thing/', RegistThingView.as_view(), name='regist_thing'),
  path('thing_detail/<int:pk>', ThingDetailView.as_view(), name='thing_detail'),
  path('confirm_achieved_thing/<int:pk>', ConfirmAchievedThingView.as_view(), name='confirm_achieved_thing'),
  path('update_thing/<int:pk>', ThingUpdateView.as_view(), name='update_thing'),
  path('delete_thing/<int:pk>', ThingDeleteView.as_view(), name='delete_thing'),
  path('achieved_list/', AchievedListView.as_view(), name='achieved_list'),
  path('achieved_thing_detail/<int:pk>', AchievedThingDetailView.as_view(), name='achieved_thing_detail'),
  path('delete_achieved_thing/<int:pk>', AchievedThingDeleteView.as_view(), name='delete_achieved_thing'),
  path('overdue_list/', OverdueListView.as_view(), name='overdue_list'),
]