#
# Example file for working with classes
# LinkedIn Learning Python course by Joe Marini edited by CE for learning purposes only!
#

class Vehicle(): ## base class is called Vehicle, has bodystyle property
    def __init__(self, bodystyle):
        self.bodystyle = bodystyle ## bodystyle is a parameter; we thus define a property on the class to hold the value 

    ##we can also add functions. classes don't just  hold data
    def drive(self, speed):
        self.mode = "driving"
        self.speed = speed

# create other class Car that derive values from the class Vehicle, inherits from Vehicle
class Car(Vehicle):
    def __init__(self, enginetype):
        super().__init__("Car") ##initialize the super class aka parent class; here we initialize the bodystyle of the super class
        self.wheels = 4 ## properties specific to the class
        self.doors = 4
        self.enginetype = enginetype
    
    def drive(self, speed):
        super().drive(speed)
        print("Driving mois", self.enginetype, "rod car at", self.speed)

# create other class Motorcycle that derive values from the class Vehicle
class Motorcycle(Vehicle):
    def __init__(self, enginetype, hassidecar):
        super().__init__("Motorcycle")
        if (hassidecar):
            self.wheels = 3
        else:
            self.wheels = 2
        self.doors = 0
        self.enginetype = enginetype

    def drive(self, speed):
        super().drive(speed)
        print("Driving mois", self.enginetype, "hotrod motorcycle at", self.speed)

##Having defined our classes of Car and Motorcycle, create specific objects of those classes types
car1 = Car("petrol")
car2 = Car("electric")
mc1 = Motorcycle("petrol", True)
mc2 = Motorcycle("electric", False)
mc3 = Motorcycle("diesel", False)

##Using the dot notation, we can get properties of each of the objects we created

print("Car1 has a ", car1.enginetype, "engine")
print("Car1 has ", car1.doors, "doors")
print("Car1 has ", car1.wheels, "wheels", end="\n\n")

print("Car2 uses ", car2.enginetype, "fuel")
print("Car2 has ", car2.doors, "doors")
print("Car2 has ", car2.wheels, "wheels", end="\n\n")

print("Motorcycle1 runs on ", mc1.enginetype)
print("Motorcycle1 has ", mc1.wheels, "wheels", end="\n\n")

print("Motorcycle1 runs on ", mc2.enginetype)
print("Motorcycle1 has ", mc2.wheels, "wheels", end="\n\n")

car1.drive(45)
car2.drive(55)
print(end="\n")

mc1.drive(79)
mc1.drive(99)
mc1.drive(109)


