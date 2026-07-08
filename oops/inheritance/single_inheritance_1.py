#single inheritance
class dad:
    def obj(self):
        print("this is dad mobile")
        
class son (dad):
    def lap(self):
        print("this is son laptop")
        
ram=son()
ram.obj()
ram.lap()
    