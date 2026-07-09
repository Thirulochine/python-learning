class Vehicle():
    def start(self):
        print("Vehicle Started")
    
class Car(Vehicle):
    def start(self):
        print("Car started")
        
cc=Car()
cc.start()