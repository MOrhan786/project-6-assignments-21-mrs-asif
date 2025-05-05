#2. Using cls
#Assignment:
#Create a class Counter that keeps track of how many objects have been created. Use a class variable
 #and a class method with cls to manage and display the count.

class Counter:
    count = 0  # Class variable to track number of objects

    def __init__(self):
        Counter.count += 1  # Increment count when a new object is created

    @classmethod
    def display_count(cls):
        print(f"My total objects created are: {cls.count}")

# Example usage
obj1 = Counter()
obj2 = Counter()
obj3 = Counter()
obj4 = Counter()

Counter.display_count()  # Output: Total objects created: 3
