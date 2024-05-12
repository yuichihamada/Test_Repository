#演習5

from abc import abstractmethod, ABCMeta

class Animal(metaclass = ABCMeta):
  
  # def __init__(self, name):
  #   self.name = name
  
  @abstractmethod
  def speak(self):
    pass

class Dog(Animal):
  
  def speak(self):
    print('わん')

class Cat(Animal):
  
  def speak(self):
    print('にゃー')

class Sheep(Animal):
  
  def speak(self):
    print('めー')

class Other(Animal):
  
  def speak(self):
    print('そんな動物いない')


num = input('1:犬 2:猫 3:羊 好きな動物の数字を入力してください')
if num == '1':
  animal = Dog()
elif num == '2':
  animal = Cat()
elif num == '3':
  animal = Sheep()
else:
  animal = Other()

animal.speak()