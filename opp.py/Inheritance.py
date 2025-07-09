# super is new model to take acces from father 
# syntax using this super().__init__() are use take aceese from fathher 
class Car:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model

    def full_name(self):
        return f"{self.brand} {self.model}"

class ElectriceCar(Car):
    def __init__(self,brand,model,battery_size):
        super().__init__(brand,model)
        self.battery_size = battery_size

my_tesla = ElectriceCar("Tesla","model S","85kwh")
print(my_tesla.model,"brand")
print(my_tesla.brand)
print(my_tesla.battery_size)
     

