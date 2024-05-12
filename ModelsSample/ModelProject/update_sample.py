import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ModelProject.settings')
from django import setup
setup()

from ModelApp.models import Person
from django.utils import timezone
import pytz
from datetime import date

#一つずつ丁寧に更新
person = Person.objects.get(id=1)
print(person)
person.birthday = date(2001, 1, 1)
person.update_at = timezone.datetime.now(pytz.timezone('Asia/Tokyo'))
person.save()

#複数を一つずつ更新
persons = Person.objects.filter(first_name='Taro')
for person in persons:
  person.first_name = person.first_name.lower()
  person.update_at = timezone.datetime.now(pytz.timezone('Asia/TOkyo'))
  # person.save()

#いっぺんに更新
Person.objects.filter(first_name='Saburo').update(
  web_site ='http://sample.jp',
  update_at = timezone.datetime.now(pytz.timezone('Asia/TOkyo'))
)
