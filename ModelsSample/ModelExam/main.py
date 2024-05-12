import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ModelExam.settings')
from django import setup
setup()

from ModelApp.models import Tests, Test_results, Students, Classes
import random

classes = ['classA', 'classB', 'classC', 'classD', 'classE', 'classF', 'classG', 'classH', 'classI', 'classJ']

students = ['studentA', 'studentB', 'studentC', 'studentD', 'studentE', 'studentF', 'studentG', 'studentH', 'studentI', 'studentJ']

tests = ['数学', '英語', '国語']

for cla in classes:
  c = Classes(name = cla)
  c.save()
  for student in students:
    s = Students(
      name = student, 
      classes = c, 
      grade = 1)
    s.save()

for test in tests:
  t = Tests(name = test)
  t.save()

for student_id in Students.objects.all():
  for test_id in Tests.objects.all():
    t = Test_results(
      student = student_id,
      test = test_id,
      score = random.randint(50,100)
    )
    t.save()