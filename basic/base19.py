# enumerate, zip, while

fruits = ['grape', 'Pine', 'Apple']

for index,value in enumerate(fruits):
  print('index = {}'.format(index))
  print('value = {}'.format(value))
  
ClassA = ['Taro', 'Hanako', 'Jiro']
ClassB = ['Katsuo', 'Wakame', 'Taro']

for a,b in zip(ClassA, ClassB):
  print('ClassA student: {}'.format(a))
  print('ClassB student: {}'.format(b))

count = 0
while count < 10:
  print(count)
  count += 1