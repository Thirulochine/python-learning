class company():
    def __init__(self):
        self.__companyname="Zoho"       #private means __
    
    def display(self):
        print(self.__companyname)   
        
cc=company()
cc.display() 