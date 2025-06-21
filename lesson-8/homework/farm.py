#homework 8
class animal:
  def __init__(self, breed, color,age):
    self.breed= breed
    self.color = color
    self.age = age
  def __str__(self):
    print(self.breed , self.color,self.age)
  def move(self):
    print("just running")

class cat(animal):
  def move(self):
    print("the cat is sleeping")
class horse(animal):
  def move(self):
    print("the horse is running")

class dog(animal):
  def move(self):
    print("the dog is barking")

Matilda = cat("Ragdoll", "white",2)   
Reks = dog("bulldog", "brown",3) 
Luna = horse("draft", "dlack",5)     

for x in (Matilda, Reks, Luna):
  x.move()
