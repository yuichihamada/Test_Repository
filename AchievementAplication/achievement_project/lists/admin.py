from django.contrib import admin
from . models import (
  WantItems, ToDoThings, AchievedThings
)


admin.site.register(
  [WantItems, ToDoThings, AchievedThings]
)