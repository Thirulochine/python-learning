class phone:
    def __init__ (self,brand,price,chargetype):         #self is a reference variable which refers to the current object
        self.brand=brand                                #self. is the instance variable which is used to acces the instance variable of the class
        self.price=price                                #given by user is self 
        self.chargetype=chargetype
        
    def display(self):
        print("Brand is ",self.brand)
        print("Price is ",self.price)
        print("Charge type is ",self.chargetype)
        
sam=phone("Samsung",200000,"Type C")
sam.display()

realme=phone("Realme",150000,"Type B")
realme.display()

infinix=phone("Infinix",100000,"Type A")
infinix.display()