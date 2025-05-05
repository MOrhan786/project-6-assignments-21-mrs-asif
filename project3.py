#3. Public Variables and Methods
#Assignment:
#Create a class Car with a public variable brand and a public method start(). 
#Instantiate the class and access both from outside the class.

class Car:
    def __init__(self, brand):
        self.brand = brand  # Public variable

    def start(self):
        print(f"{self.brand} is starting...")  # Public method

# Instantiate the class
my_car = Car("Toyota")

# Access the public variable
print("Car brand:", my_car.brand)

# Call the public method
my_car.start()
