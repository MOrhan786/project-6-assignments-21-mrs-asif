# 19. callable() and __call__()
#Assignment:
#Create a class Multiplier with an __init__() to set a factor. Define a __call__() method that multiplies an input by the factor. Test 
#it with callable() and by calling the object like a function.

class Multiplier:
    def __init__(self, factor):
        self.factor = factor
    
    # __call__ method to multiply the input by the factor
    def __call__(self, x):
        return x * self.factor

# Creating an instance of the Multiplier class
multiplier_by_5 = Multiplier(5)

# Checking if the object is callable
print(callable(multiplier_by_5))  # Output: True

# Calling the object like a function
result = multiplier_by_5(10)
print("10 multiplied by 5:", result)
