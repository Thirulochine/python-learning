class Fruit: 
    def __init__(self, name, color):
        self.name=name
        self.color=color
    def display(self):
        #print("Name of the fruit:",self.name)
        #print("Color of the fruit:",self.color)
        return "Name of the fruit: "+self.name+"\nColor of the fruit: "+self.color
fruit=input("Enter the name of the fruit:")
color=input("Enter the color of the fruit:") 
      
fr1=Fruit(fruit,color)
print(fr1.display())

