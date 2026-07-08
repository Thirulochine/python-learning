class grandpa():
    def land(self):
        print("grandpa has land")
        
class dad(grandpa):
    def house(self):
        print("daddy has house")
        
class son(dad):
    def car(self):
        print("son has car")
        
#grandpa
pandu=grandpa()
print("grandpa info\n")
pandu.land()
print("\n")
#dad
senthil=dad()
print("dad info\n")
senthil.land()
senthil.house()
print("\n")
#son
mohan=son()
print("son info\n")
mohan.land()
mohan.house()
mohan.car()
