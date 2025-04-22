# lets assume in website there are so many categories of products.

from enum import Enum 

class Color(Enum):
    RED=1
    BLUE=2
    GREEN=3

class Size(Enum):
    SMALL=1
    MEDIUM=2
    LARGE=3


class Products:
    def __init__(self,name,color,size):
        self.name=name
        self.color=color
        self.size=size

#before ocp principle
class ProductFilter:
    def __init__(self,products):
        self.products=products

    def filter_by_color(self,color):
        for p in self.products:
            if p.color==color:
                yield p
    
    def filter_by_size(self,size):
        for p in self.products:
            if p.size==size:
                yield p


#after ocp

class Specification:
    def is_satisfied(self,item):
        pass

class ColorSpecification(Specification):
    def __init__(self,color):
        self.color=color

    def is_satisfied(self,item):
        return self.color==item.color

class Filter:
    def filter(self,items,spec):
        pass

class BetterFilter(Filter):
    def filter(self,items,spec):
        for item in items:
            if spec.is_satisfied(item):
                yield item



# house=Products("house",Color.GREEN,Size.LARGE)
# tree=Products("tree",Color.GREEN,Size.MEDIUM)
# p=[house,tree]
# pf=ProductFilter(p)
# for p in pf.filter_by_size(Size.LARGE):
#     print(p.name)



#after ocp
house=Products("house",Color.GREEN,Size.LARGE)
tree=Products("tree",Color.GREEN,Size.MEDIUM)
p=[house,tree]
bf =BetterFilter()
spec=ColorSpecification(Color.GREEN)

for i in bf.filter(p,spec):
    print(f'{i.name}')
