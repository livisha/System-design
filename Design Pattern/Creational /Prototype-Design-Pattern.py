'''
The concept is to copy an existing object rather than creating a new instance. because creating new object may be costly
ex- new bike without using old one
'''
import copy
class Employee:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def __str__(self):
        return f'name: {self.name} \nage: {self.age}'

    def clone(self):
        return copy.deepcopy(self)

original = Employee("livisha",24)
clone1=original.clone()
clone2= original.clone()

clone1.name="rajveer"
clone2.age=34
print(original)
print(clone1)
print(clone2)
