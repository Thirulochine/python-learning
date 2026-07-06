class Student:
    def __init__(self,name,register_number):
        self.name = name
        self.register_number = register_number
    def display(self):
        print("Name:", self.name)
        print("Register Number:", self.register_number)

obj1=Student("Shastika", "123456")           #constructor is called when object is created
obj2=Student("John", "654321")

obj1.display()
obj2.display()