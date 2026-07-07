class phone:
    chargetype = "Type-C"           #class variable 
    def __init__(self,brand,price):
        self.brand = brand
        self.price = price
        
    def show(self):
        print("Brand:",self.brand)
        print("Price:",self.price)
        print("Charge Type:",self.chargetype)
 
 
#phone.chargetype="Type-B"     #also modify cl variable value by this way    
sam=phone("Samsung", 20000)
sam.show()

infinix=phone("Infinix", 15000)
infinix.show()
