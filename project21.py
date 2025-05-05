# 21. Make a Custom Class Iterable
#Assignment:
#Create a class Countdown that takes a start number. Implement __iter__() and __next__()
#
#  to make the object iterable in a for-loop, counting down to 0.

class Countdown:
    def __init__(self, start):
        self.start = start
        self.current = start

    # __iter__ method to return the iterator object itself
    def __iter__(self):
        return self
    
    # __next__ method to return the next number in the countdown
    def __next__(self):
        if self.current <= 0:
            raise StopIteration  # Stop the iteration when we reach 0
        self.current -= 1
        return self.current

# Creating an instance of Countdown starting from 5
countdown = Countdown(5)

# Iterating through the Countdown object using a for loop
for number in countdown:
    print(number)
