class Student:
    def __init__(self):
        self.name = ""
        self.register_number = ""
    def display(self):
        print("Name:", self.name)
        print("Register Number:", self.register_number)

obj1=Student()
obj2=Student()

obj1.name = "Shastika"              #constructor is called when object is created
obj1.register_number = "123456"

obj2.name = "John"
obj2.register_number = "654321"

obj1.display()
obj2.display()