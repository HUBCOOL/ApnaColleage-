class Car:
    def __init__(self,brand,model,bachhi,colour):
        self.brand = brand
        self.model = model
        self.bacchi = bachhi
        self.colour = colour
# self is in simple  world we use to connect with object (phone to connect with people)
    def full_name(self):
        return f"{self.brand} {self.model}"
    def group(self):
        return f"{self.bacchi} {self.colour}"


my_car = Car("Auto","tata","shubham","Yellow")
print(my_car.model)
print(my_car.full_name())
print(my_car.group())

