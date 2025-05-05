# 14. Aggregation
#Assignment:
#Create a class Department and a class Employee. Use aggregation by having a Department object store
# a reference to an Employee object that exists independently of it.

class Employee:
    def __init__(self, name):
        self.name = name

    def display(self):
        print(f"Employee Name: {self.name}")

class Department:
    def __init__(self, dept_name, employee):
        self.dept_name = dept_name
        self.employee = employee  # Aggregation: reference to existing Employee object

    def show_details(self):
        print(f"Department: {self.dept_name}")
        self.employee.display()  # Access Employee method

# Example usage
emp1 = Employee("Ali")  # Independent Employee object

dept1 = Department("HR", emp1)  # Department has reference to emp1
dept1.show_details()

# Employee still exists independently
emp1.display()
