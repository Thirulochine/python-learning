class Student:
    def __init__(self):
        self.name = "Shastike"
        self.register_number = "123456"
    def display(self):
        print("Name:", self.name)
        print("Register Number:", self.register_number)

obj=Student()
obj.display()