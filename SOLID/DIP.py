from enum import Enum
from abc import abstractmethod
class Relationship(Enum):
    PARENT=0
    CHILD=1
    SIBLINGS=2

class Person:
    def __init__(self,name):
        self.name=name
    
class RelationsShipBrowser:
    @abstractmethod
    def find_all_children_of(self, name): pass

class Relationships(RelationsShipBrowser):
    def __init__(self):
        self.relations=[]

    def add_parent_to_child(self,parent,child):
        self.relations.append((parent,Relationship.PARENT,child))
        self.relations.append((child,Relationship.CHILD,parent))
    
    def find_all_children_of(self, name):
        for r in self.relations:
            if r[0].name == name and r[1] == Relationship.PARENT:
                yield r[2].name

class Research:
    # def __init__(self,relationships):
    #     relation=relationships.relations
    #     for i in relation:
    #         if i[0].name=='john' and i[1]==Relationship.PARENT :
    #             print(f'john has a child callled {i[2].name}')
     def __init__(self, browser):
        for p in browser.find_all_children_of("john"):
            print(f'John has a child called {p}')

john=Person('john')
child1=Person("chris")

r=Relationships()
r.add_parent_to_child(john,child1)

Research(r)
