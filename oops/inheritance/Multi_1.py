#multiple inheritance 
class dad():
    def phone(self):                        #2 class assested by 1 class
        print("dad has phone")
        
class mom():
    def sweet(self):
        print("mom has sweets")
        
class son(dad,mom):
    def lap(self):
        print("son has laptop")
        
raghul=son()
raghul.phone()
raghul.sweet()
raghul.lap()