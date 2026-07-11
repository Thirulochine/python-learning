class a():
    def __init__(self):
        self._company="wipro"     #protector
        
class b(a):
    def display(self):            #child class also access
        print(self._company)
    
bb=b()
bb.display()