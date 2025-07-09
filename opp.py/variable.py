class parent:
    def __init__(self,name):
        self.name=name

    def greet(self):
        print(f"hello from {self.name}")


class child(parent):
    def __init__(self,name,age):
        super().__init__(name)
        self.age=age

    def greet(self):
        super().greet()
        print(f"And i am {self.age}")

child =child("Alice",10)
child.greet()



