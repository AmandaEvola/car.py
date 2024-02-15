class Car:
    def __init__(self, make, model, year, color):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.speed = 0



    def accelerate(self, increment):
        self.speed += increment

    def brake(self, decrement):
        self.speed -= decrement
        if self.speed < 0:
            self.speed = 0

    def display_speed(self):
        print("Current speed:", self.speed, "mph")

# Creating an instance of the Car class
my_car = Car("Toyota", "Camry", 2022, "Blue")

# Accelerating the car
my_car.accelerate(30)
my_car.display_speed()

# Braking the car
my_car.brake(10)
my_car.display_speed()
