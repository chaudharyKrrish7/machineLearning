class Car:
    total_Car =   0
    def __init__(self, brand, model):
        self.__brand = brand
        self.model = model
        Car.total_Car += 1
    def full_name(self):
        return f"{self.brand} {self.model}"
    
    def get_brand(self):
        return self.__brand + "!"
    
    def fuel_type(self):
        return "Petrol or diesel"
    @staticmethod
    def general_desc():
        return "Cars are mean of transportation"

class ElectricCar(Car):  #inheritance
    def __init__ (self , brand, model, battery_size):
        self.battery_size = battery_size
        super().__init__(brand, model)

    def fuel_type(self):
        return "Electric Charge"

# my_car = Car("Toyota", "Camry")
# print(my_car.brand)
# print(my_car.model)
# print(my_car.full_name())
 
# my_car_new = Car("Honda", "Civic")
# print(my_car_new.brand)
# print(my_car_new.model) 


my_tesla = ElectricCar("Tesla", "Model S", 100)
print(isinstance(my_tesla, Car))  # True
print(isinstance(my_tesla, ElectricCar))  # True
# print(my_tesla.__brand)
print(my_tesla.get_brand())
print(my_tesla.fuel_type())
# print(my_tesla.model)
# print(my_tesla.battery_size) 
# print(my_tesla.full_name())

safari = Car("Safari", "Land Cruiser")
print(Car.total_Car)
print(safari.fuel_type())


print(safari.general_desc())
# print(Car.general_desc())
print(my_tesla.general_desc())



class Battery:
    def battery_info(self):
        return "this is battery"
class Engine:
    def engine_info(self):
        return "this is engine"
class Ecar(Battery, Engine , Car):
    def __init__ (self , brand, model, battery_size):
        # self.battery_size = battery_size
        super().__init__(brand, model) 

my_new_tesla = Ecar("Tesla", "Model 3", 75)
print(my_new_tesla.battery_info())
print(my_new_tesla.engine_info())