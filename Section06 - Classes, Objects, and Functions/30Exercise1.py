#Create a class called Car that has the following attributes:
#brand, color, fuel, and engine_size
#Create the __init__ function that assigns the parameters of the class to the class's attributes
#Create another function show_characteristics that uses print to display on screen
#the characteristics (or attributes) of the car.
#Create an object car1 from the class Car with the attributes "Opel", "red", "gasoline", "1.6"
#Execute the function show_characteristics of the object car1

""" class Car:
    def __init__(self,brand,color,fuel,engine_size):
        self.brand = brand
        self.color = color
        self.fuel = fuel
        self.engine_size = engine_size
    
    def show_characteristics(self):
        print(f"The car's brand is {self.brand}, its color is {self.color}, it uses {self.fuel} as fuel, and it has a {self.engine_size} engine.")
    
car1 = Car("Opel","Red","Gasoline","1.6")

car1.show_characteristics() """


class Car:
    def __init__(self, brand, color, fuel, engine_size):
            self.brand = brand
            self.color = color
            self.fuel = fuel
            self.engine_size = engine_size

    def show_characteristics(self):
        print("The car's brand is {} in a color {} that uses the fuel {}, and it has a {} engine".format(self.brand,self.color,self.fuel,self.engine_size))

car1 = Car("opel","red","gasoline","1.6")
car1.show_characteristics()