import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ModelProject.settings')
from django import setup
setup()

from ModelApp.models import Students

#全件取得
# print(Students.objects.all())

#頭5件取得
# print(Students.objects.all()[:5])

#5件目より後取得
# print(Students.objects.all()[5:])

#5~7件目
# print(Students.objects.all()[4:7])

# print(Students.objects.all()[4:7].query)

# 一番最初の1件
# print(Students.objects.first())

#等価のものだけに絞り込む
# print(Students.objects.filter(name='太郎'))
# print(Students.objects.filter(age=17))

# AND条件
# print(Students.objects.filter(name='太郎', pk__gt=13))
# print(Students.objects.filter(name='太郎', pk__lt=19))
# print(Students.objects.filter(name='太郎', pk__gte=13))
# print(Students.objects.filter(name='太郎', pk__lte=19))

#前方一致、後方一致
# print(Students.objects.filter(name__startswith='太'))
# print(Students.objects.filter(name__endswith='郎'))

# or
from django.db.models import Q

print(Students.objects.filter(Q(name = '太郎') | Q(pk__gt=19)))