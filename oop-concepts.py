# Inheritance - DONE
# Polymorphism (Overloading, Overriding) -  DONE
# Abstraction - DONE
# Encapsulation - DONE

from typing import overload

class VehicleEngine():
    def create_engine():
        print("creating engine")

    class Meta:
        abstract = True

class Vehicle(VehicleEngine):
    
    def __init__(self, name, color, model):
        self.name = name 
        self.color = color 
        self.model = model 

    def move(self):
        print("moving .....")

    def stop(self):
        print("breaked....")


class Car(Vehicle):
    ... 

class Bike(Vehicle): 
    pass

civic = Car(name="Civic", color="red", model="vv")
civic.move()


class Animal():
    def __init__(self, name, color):
        self.name = name 
        self.color = color 
    
    def move(self):
        print("swimming...")

class Bird(Animal):
    feathers = 10 

    @overload
    def move(self):
        print("flying...")
    
    @overload
    def move(self, method, me):
        print(method, me)
    
    def move(self, method):
        print(method)
    
    
    

print("BIRD")
blueblue = Bird(name="Blueblue", color="pink")
blueblue.move("crawl")


