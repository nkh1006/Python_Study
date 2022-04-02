# Object Orientated Programming in Python

class Dog:
  def __init__(self, name):
    self.name = name
    print(name)
    
  def get_name(self):
    return self.name
  
  def get_age(self):
    return self.get_age
  
  def set_age(self, age):
    self.age = age
    
d = Dog("Tim")
print(d.name)
d2 = Dog("Bill")
print(d2.name)