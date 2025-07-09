class Car:
    def __init__(self):
        self.make = None
        self.model = None

class CarBuilder:
    def __init__(self):
        self.car = Car()

    def set_make(self, make):
        self.car.make = make
        return self
    
    def set_model(self, model):
        self.car.model = model
        return self
    
    def build(self):
        return self.car
    
    
builder = CarBuilder()
car = (builder.set_make("Toyota").set_model("Corolla").build())


