#Liscov substitute principle

class Rectangle:
    def __init__(self,width,height):
        self._height=height
        self._width=width

    @property
    def width(self):
        return self._width
    
    @property
    def height(self):
        return self._height

    @width.setter
    def width(self,value):
        self._width=value
    
    @height.setter
    def height(self,value):
        self._height=value

    @property
    def area(self):
        return self._width * self._height

class Square(Rectangle):
    def __init__(self,size):
        Rectangle.__init__(self,size,size)

    @Rectangle.width.setter
    def width(self,value):
        self._width=self._height=value

    @Rectangle.height.setter
    def height(self,value):
        self._width=self._height=value
    


def use_init(rc):
    w=rc.width
    rc.height=10
    a=int(w*10)
    print(f'the expected is {a} and got is {rc.area}')

rc=Rectangle(3,2)
use_init(rc)

Sq=Square(5)
use_init(Sq)