class Lap:
    def __init__ (self):
        self.ram = 0
        self.processor = ""
        
    def info(self):
        print("Ram : ",self.ram)
        print("Processor : ",self.processor)    
        
dell = Lap ()
dell.ram = 8
dell.processor = "i5"

dell.info()