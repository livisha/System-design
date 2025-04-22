class Machine:
    def print(self,document):
        pass
    def fax(self,document):
        pass

class Printer(Machine):
    def print(self,document):
        pass
    def fax(self,document):
        pass
        # no need of this function 
    

#we will follor interface segregation principle

class Printer:
    def print(self,document):
        pass

class Faxing:
    def fax(self,document):
        pass


class oldfashionedPrint(Printer):
    def print(self,document):
        print(document)
        