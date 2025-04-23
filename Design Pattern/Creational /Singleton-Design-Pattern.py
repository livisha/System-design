'''
when we want to create object only one time in whole application and want to use that object everywhere then singleton is used
'''

class Singleton:
    _instance=None
    def __new__(cls):
        if cls._instance==None:
            print("new object")
            cls._instance=super().__new__(cls)
        else:
            print("Using existing object")
        return cls._instance
    
    def __init__(self):
        print("Init called")

s1 = Singleton()
s2 = Singleton()
print(s1==s2)
