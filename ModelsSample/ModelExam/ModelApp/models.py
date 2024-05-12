from django.db import models

class Tests(models.Model):
  id = models.AutoField(primary_key = True)
  name = models.CharField(max_length=50)
  
  class Meta:
    db_table = 'tests'

class Test_results(models.Model):
  id = models.AutoField(primary_key = True)
  student = models.ForeignKey(
    'Students', on_delete = models.CASCADE
  )
  test = models.ForeignKey(
    'Tests', on_delete = models.CASCADE
  )
  score = models.IntegerField()
  
  class Meta:
    db_table = 'test_results'

class Students(models.Model):
  id = models.AutoField(primary_key = True)
  classes = models.ForeignKey(
    'Classes', on_delete = models.CASCADE
  )
  name = models.CharField(max_length=50)
  grade = models.IntegerField()
  
  class Meta:
    db_table = 'students'

class Classes(models.Model):
  id = models.AutoField(primary_key = True)
  name = models.CharField(max_length=50)
  
  class Meta:
    db_table = 'classes'