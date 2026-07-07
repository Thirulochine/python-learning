class phone:
    def __init__(self):
        self.brand=""
        self.price=0
        self.chargetype=""
        
    def getdata (self,brand,price,chargetype):
        self.brand=brand
        self.price=price
        self.chargetype=chargetype
                
    def display(self):
        print("brand :",self.brand)
        print("price :",self.price)
        print("charge type: ",self.chargetype)
        
    @staticmethod    
    def info():
        print("this is static method, inside the bracket there is no need to pass self or class anything else")
        
ee=phone()
ee.getdata("samsung",30000,"B-type")
ee.display()
ee.info()