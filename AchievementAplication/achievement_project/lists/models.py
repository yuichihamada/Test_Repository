from django.db import models
from accounts.models import Users

class WantItems(models.Model):
  name = models.CharField(max_length=150, unique=True)
  detail = models.CharField(max_length=1000)
  picture = models.FileField(null=True, default='/item.png/')
  price = models.IntegerField()
  target_date = models.DateField()
  reason = models.CharField(max_length=2000)
  user = models.ForeignKey(
    Users,
    on_delete=models.PROTECT
  )
  create_at = models.DateTimeField()
  update_at = models.DateTimeField()
  
  class Meta:
    db_table = 'wantitems'
  
  def __str__(self):
    return self.name


class ToDoThings(models.Model):
  name = models.CharField(max_length=150, unique=True)
  detail = models.CharField(max_length=1000, default=None)
  picture = models.FileField(null=True, default='/todo.png/')
  price = models.IntegerField()
  target_date = models.DateField()
  reason = models.CharField(max_length=2000)
  user = models.ForeignKey(
    Users,
    on_delete=models.PROTECT
  )
  create_at = models.DateTimeField()
  update_at = models.DateTimeField()
  
  class Meta:
    db_table = 'todothings'
  
  def __str__(self):
    return self.name
    

class AchievedThings(models.Model):
  name = models.CharField(max_length=150)
  detail = models.CharField(max_length=1000, default=None)
  picture = models.FileField(null=True, default='/achieved.png/')
  price = models.IntegerField()
  achieved_date = models.DateField()
  text = models.CharField(max_length=2000)
  user = models.ForeignKey(
    Users,
    on_delete=models.PROTECT
  )
  type = models.CharField(max_length=15, default=None)
  create_at = models.DateTimeField()
  update_at = models.DateTimeField()
  
  class Meta:
    db_table = 'achievedthings'