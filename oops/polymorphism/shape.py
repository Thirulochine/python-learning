class shape():
    def area(self):
        return 0
    
class rectangle(shape):
    def area(self):
        l=5
        b=10
        c=5*10
        return c


obj=rectangle()
print("Area of a rectangle : ",obj.area())