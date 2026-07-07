class phone:
    chargetype = "Type-C"           #class variable
    def __init__(self):
        self.brand = "Samsung"
        self.price = 200000
        
        
    def getdata(self,price):           #instance method
        self.price=price
        
    @classmethod
    def chargetype(cls):               #class method
        cls.chargetype="Type-B"
        print("Charge Type:",cls.chargetype)

sam=phone()
sam.getdata(250000)

phone.chargetype()