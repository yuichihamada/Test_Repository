import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ModelProject.settings')
from django import setup
setup()

from ModelApp.models import Places, Restaurants

places = [
  ('Motomachi', 'Yokohama'), ('Tsukiji', 'Tokyo')
]

restaurants = ['restaurants A', 'restaurants B']


for place_name, place_address in places:
  p = Places(
    name=place_name,
    adress=place_address
  )
  p.save()
  for restaurant_name in restaurants:
    # r = Restaurants(
    #   place=p,
    #   name=restaurant_name
    # )
    # r.save()
    Restaurants.objects.create(
      place=p, name=restaurant_name
    )