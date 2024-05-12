# Private変数

class Human:
  
  __class_val = 'Human'
  
  def __init__(self, name, age):
    self.__name = name
    self.__age = age
  
  def print_msg(self):
    print('name = {}, age = {}'.format(self.__name, self.__age))


human = Human('Taro', 15)
# print(human.__name)
# print(human._Human__name)
human.print_msg()