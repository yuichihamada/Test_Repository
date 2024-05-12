##dictの連結

# dictの作成
ages = {
  'Taro': 21,
  'Jiro': 31
}

ages_2 = {
  'Saburo': 18,
  'Hanako': 21,
  'Taro': 35
}

#update(python<=3.8)

ages_3 = {**ages, **ages_2}

print(ages_3)

def name_age(name, age):
  print('name = {}'.format(name))
  print('age = {}'.format(age))

man = {
  'name': 'Taro',
  'age': 23
}

name_age(**man)

# 3.9での連結方法 ({**dict1, **dict2} => dict1 | dict2)
ages_4 = ages | ages_2

print(ages_4)