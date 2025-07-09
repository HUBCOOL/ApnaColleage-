class CPU:
    def start(self):
        print("cpu started")

class Memory:
    def load(self):
        print("Memory loaded")

class HardDrive:
    def read(self):
        print("HardDrive read")

class ComputerFacade:
    def __init__(self):
        self.cpu=CPU()
        self.memory=Memory()
        self.hard_drive=HardDrive()

    def start_computer(self):
        self.cpu.start()
        self.memory.load()
        self.hard_drive.read()


computer = ComputerFacade()
computer.start_computer()

  

