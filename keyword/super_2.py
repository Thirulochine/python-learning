class a():
    def __init__(self):
        print("a is displayed")
        
    def num(self):
        print("from a class")
        
class b():
    def __init__(self):
        super().__init__()
        print("b is displayed")
        
    def num(self):
        print("from b class") 
        
'''class c(a,b):               #()inside 1st works as super
    def __init__(self):
        super().__init__()
        print("c is displayed")               
        
    def num(self):
        print("from c class")'''
        
class c(b,a):                 #()inside 1st works as super
    def __init__(self):
        super().__init__()
        print("c is displayed")
        
    def num(self):
        print("from c class")

obj=c()
   