'''when there is superclass and subclass and we want to get object of subclass based on input and requirement. 
then we create factory class which takes the responsiblity of creating object of class based on input

Advantage
1. focus on creating object for interface rather than implementation.
2. Loose coupling, more robust code
'''

from abc import abstractmethod
class Employee:
    @abstractmethod
    def getSalary(self):
        pass

class Android(Employee):

    def getSalary(self):
        print(f"The android salary is : ")
        return 40000

    
class WebDeveloper(Employee):

    def getSalary(self):
        print(f"The web developer salary is : ")
        return 50000


class Factory:

    def getEmployee(self,name):
        if name=="Android":
            return Android()

        elif name=="Web":
            return WebDeveloper()

        else:
            return null


f=Factory()
obj=f.getEmployee("Web")
sal=obj.getSalary()
print(f'Salary: {sal}')
