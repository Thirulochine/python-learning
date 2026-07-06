class Calculator:
    def add(self,x,y):
        print("Addition")
        self.x=x
        self.y=y
        print("Sum is : ",self.x+self.y)
    def sub(self,a,b):
        print("Substraction")
        self.a=a
        self.b=b
        print("Difference is : ",self.a-self.b)
    
    def mul(self,c,b):
        self.c=c
        self.b=b
        print("Multiplication")
        print("Product is : ",self.c*self.b)

    def div(self,f,t):
        print("Division")
        self.f=f
        self.t=t
        print("Quotient is : ",self.f/self.t)
   
obj=Calculator() 
obj.add(4,4)
obj.sub(10,5)
obj.mul(2,3)
obj.div(10,2)