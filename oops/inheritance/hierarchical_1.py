#4. Hierarchical Inheritance
class dad():
    def money (self):
        print("dad has money")
        
class son1(dad):
    def phone (self):
        print("son 1 has iphone")

class son2(dad):
    def phone(self):
        print("son 2 has samsung phone")
        
class son3(dad):
    def phone(self):
        print("son 3 has vivo phone")
        
s1=son1()
s2=son2()
s3=son3()

s1.money()
s1.phone()

s2.money()
s2.phone()

s3.money()
s3.phone()