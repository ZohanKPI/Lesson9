
class Auto:
    def __init__(self, mark, colour, volume):
        self.mark = mark
        self.colour = colour
        self.volume = volume

    def print_characteristics(self):
        print(f"Mark: {self.mark}")
        print(f"Colour: {self.colour}")
        print(f"Volume: {self.volume}")
    def drive_forward(self):
        print("Car driving forward")
    def drive_backward(self):
        print("Car driving backward")

class Car(Auto):
    def __init__(self, mark, colour, volume):
        super().__init__(mark, colour, volume)
    def drive_left(self):
        print("Car driving left")
    def drive_right(self):
        print("Car driving right")

my_car = Car("Mercedes", "Silver", 3.7)
my_car.print_characteristics()
my_car.drive_forward()
my_car.drive_backward()
my_car.drive_left()
my_car.drive_right()
