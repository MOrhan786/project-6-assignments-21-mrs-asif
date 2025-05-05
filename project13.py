#  13. Composition
#Assignment:
#Create a class Engine and a class Car. Use composition by passing an Engine object to the Car class during 
#initialization. Access a method of the Engine class via the Car class.


class Engine:
    def start(self):
        print("Engine is starting... Vroom Vroom!")

class Car:
    def __init__(self, engine):
        self.engine = engine  # Composition: Engine object inside Car

    def start_car(self):
        print("Starting the car...")
        self.engine.start()   # Access Engine's method through Car

# Example usage
my_engine = Engine()
my_car = Car(my_engine)

my_car.start_car()
