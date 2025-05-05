#7. Access Modifiers: Public, Private, and Protected
#Assignment:
#Create a class Employee with:

#a public variable name,

#a protected variable _salary, and

#a private variable __ssn.

#Try accessing all three variables from an object of the class and document what happens.












class Employee:
    def __init__(self, name, salary, ssn):
        self.name = name        # Public variable
        self._salary = salary   # Protected variable (convention)
        self.__ssn = ssn        # Private variable (name mangling)

# Create an object
emp1 = Employee("Ali", 50000, "123-45-6789")

# Access public variable
print("Name:", emp1.name)

# Access protected variable
print("Salary:", emp1._salary)

# Try to access private variable directly
try:
    print("SSN:", emp1.__ssn)
except AttributeError as e:
    print("Error accessing __ssn:", e)

# Access private variable using name mangling (possible but not recommended)
print("Accessing private SSN (with name mangling):", emp1._Employee__ssn)





