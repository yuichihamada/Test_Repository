# DIctionary(辞書型)

car = {'brand': 'Toyota', 'model': 'Prius', 'year': 2015 , 1: 100}

print(car['brand']) #Toyota
print(car.get('bran', 'Does not exist'))

print(car.get(1))

print(car.keys()) #キー一覧
print(car.values()) #値一覧
print(car.items()) #キー + 値

for k, v in car.items():
  print('key = {}, value = {}'.format(k, v))
  
if 'brand' in car:
  print('carのブランドは{}'.format(car['brand']))
  