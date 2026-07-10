class a():
    def __init__(self):
        self._company="wipro"     #protector
        
class b(a):
    def display(self):
        print(self._company)
    
bb=b()
bb.display()