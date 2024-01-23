class Vehicle:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

    def display_info(self):
        print(f"Brand: {self.brand}\nYear: {self.year}")

class Car(Vehicle):
    def __init__(self, brand, year, model):
        super().__init__(brand, year)
        self.model = model

class Motorcycle(Vehicle):
    def __init__(self, brand, year, probeg):
        super().__init__(brand, year)
        self.probeg = probeg

car = Car('Toyota', 2022, 'Camry')
moto = Motorcycle('Ducatti', 2020, '19.000')

car.display_info()
moto.display_info()
