#Class and Objects 

class Chairclass:
    color = "white"
    cost = 100

objectchair1 = Chairclass()
objectchair1.color

print (objectchair1.color)
print (objectchair1.cost)

objectchair2 = Chairclass()
objectchair2.color = "green"
objectchair2.cost = 150

print (objectchair2.color)
print (objectchair2.cost)

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def greeting(self):
        print ("Hi, my name is {self.name} and I am {self.age} years old")


persona1 = Person("John",37)
print (persona1.name)
print (persona1.age)
persona1.greeting()