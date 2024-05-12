from django.db import models
from django.contrib.auth.models import(
  BaseUserManager, AbstractBaseUser, PermissionsMixin
)
from django. urls import reverse_lazy
from datetime import datetime


class UserManager(BaseUserManager):
  
  def create_user(self, username, email, password=None):
    if not email:
      raise ValueError('Enter Email!')
    user = self.model(
      username=username,
      email=email,
    )
    user.set_password(password)
    user.create_at = datetime.now()
    user.update_at = datetime.now()
    user.save(using=self._db)
    return user
  
  def create_superuser(self, username, email, password=None):
    user = self.model(
      username=username,
      email=email,
    )
    user.set_password(password)
    user.is_staff = True
    user.is_active = True
    user.is_superuser = True
    user.create_at = datetime.now()
    user.update_at = datetime.now()
    user.save(using=self._db)
    return user
    

class Users(AbstractBaseUser, PermissionsMixin):
  
  username = models.CharField(max_length=150, unique=True)
  email = models.EmailField(max_length=255, unique=True)
  is_active = models.BooleanField(default=True)
  is_staff = models.BooleanField(default=False)
  picture = models.FileField(null=True)
  introduction = models.CharField(max_length=1000,null=True)
  create_at = models.DateTimeField()
  update_at = models.DateTimeField()
  
  USERNAME_FIELD = 'email'
  REQUIRED_FIELDS = ['username']
  
  objects = UserManager()
  
  def get_absolute_url(self):
    return reverse_lazy('accounts:home')
  
  def __str__(self):
    return self.username