class Animal():
    def sound(self):
        print("Animal makes sound")
    
class Dog(Animal):
    def sound(self):
        print("Dog barks")
        
class Birds(Animal):
    def sound(self):
        print("Birds sings")

obj=Birds()
obj.sound()