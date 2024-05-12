from typing import Self

class User:
  
  def __init__(self, name, age):
    self.name = name
    self.age = age
  
  def compare(self: Self, other: Self) -> bool:
    return self.name == other.name and self.age == other.age
  
  def copy(self: Self) -> Self:
    return User(self.name, self.age)

user1 = User('Taro', 18)
user2 = User('Taro', 18)
msg = 'Hello'

print(user1.compare(user2))
# print(user1.compare(msg))
user3 = user1.copy()
print(user1.compare(user3))
