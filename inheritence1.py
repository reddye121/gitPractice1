class Vehicle:
    def startd(self):
        print("Starting vehicle")

class Car(Vehicle):
    def start(self):
        super().startd()
        print("car started")
        print("i always be worring with something")
        print("i need to find a solution for it")

car=Car()
car.start()