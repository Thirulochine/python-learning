class Teacher:
    def __init__(self,name,register_number):
        self.name = name
        self.register_number = register_number
    def display(self):
        print("Name:", self.name)
        print("Register Number:", self.register_number)

obj1=Teacher("Shastika", "1")           #constructor is called when object is created
obj2=Teacher("John", "2")

obj1.display()
obj2.display()