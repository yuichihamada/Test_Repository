from django.db import models

# Create your models here.

class Students(models.Model):
  id = models.AutoField(primary_key=True)
  name = models.CharField(max_length=50)
  age = models.IntegerField()
  grade = models.IntegerField()
  picture = models.FileField(upload_to= 'picture/')