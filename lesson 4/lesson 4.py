class Human:
    def __init__(self,name):
        self.name = name

class Auto:
    def __init__(self,brand):
        self.brand = brand
        self.passenger = []
    def add_passenger(self,human):
        self.passenger.append(human)
    def print_passengers_names(self):
        if self.passenger != []:
            print(f"Names of {self.brand} passenger: ")
            for passenger in self.passenger:
                print(passenger.name)
        else:
            print(f"There are not passengers in {self.brand}")

nazar = Human("Nazar")
mery = Human("Mary")

car = Auto("BMV")
car.add_passenger(nazar)
car.add_passenger(mery)
car.print_passengers_names()