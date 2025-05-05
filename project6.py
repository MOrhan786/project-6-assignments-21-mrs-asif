#6. Constructors and Destructors
#Assignment:
#Create a class Logger that prints a message when an object is created 
#(constructor) and another message when it is destroyed (destructor).

class Logger:
    def __init__(self):
        print("Logger object has been created.")

    def __del__(self):
        print("Logger object is being destroyed.")

# Example usage
log1 = Logger()

# Deleting the object explicitly (optional — otherwise happens automatically)
del log1
