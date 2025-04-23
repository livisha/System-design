'''
while creating factory design - object when onject contain may attribute:
    1. we hav to pass many arguments to create object 
    2. some parameters might ben optional 
    3. factory class takes all the responsiblity for creating object

so builder pattern be created object step by step and finally return the object

ab humko dot dot krke bhejna pdega that is easy to call

example - topping in pizza
'''

class Employee:
    def __init__(self):
        self.name=None
        self.age=None
        self.role=None
        self.salary=None

    def __str__(self):
        return f"name:{self.name} \nemail:{self.age} \nrole:{self.role} \nsalary:{self.salary}"


class EmployeeBuilder:
    def __init__(self):
        self.employee=Employee()

    def setname(self,name):
        self.employee.name=name
        return self
    
    def setAge(self, age):
        self.employee.age = age
        return self

    def setRole(self, role):
        self.employee.role = role
        return self

    def setSalary(self, salary):
        self.employee.salary = salary
        return self

    def build(self):
        return self.employee


builder=EmployeeBuilder()
employee = (
    builder
    .setname("Riyodveer")
    .setAge(25)
    .setRole("Web Developer")
    .setSalary(50000)
    .build()
)

print(employee)