'''
One more abstraction into factory design pattern
ab na spcially client code ya factory class me if else nhi dena . direct ek or object bnake uske pass krna hota hai
jese devfactory ka bnake factory me bhejna
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
    @abstractmethod
    def createEmployee(self):
        pass

class WebDevFactory(Factory):
    def createEmployee(self):
        return WebDeveloper()

class AndroidDevFactory(Factory):
    def createEmployee(self):
        return Android()


#client code
def getemployeesdetail(factory):
    emp=factory.createEmployee()
    sal=emp.getSalary()
    print(sal)

dev=WebDevFactory()
getemployeesdetail(dev)

