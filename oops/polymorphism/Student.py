class Person():
    def __init__(self,name):
        self.name=name
        
class Student(Person):
    def __init__(self,name,grade):
        super().__init__(name)
        self.grade=grade
        
    def display(self):
        print("Student Name: ",self.name)
        print("Grade: ",self.grade)
        
s1=Student("Moni","A")
s1.display()