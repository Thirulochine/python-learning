class Goa:
    name=""
    drink = ""
    def party(self):
        print("let's party in Goa")
    def beach (self):
        print("let's go to beach in Goa")

ramesh = Goa()
suresh = Goa()

ramesh.name= "Ramesh"
ramesh.drink= "No"

suresh.name= "Suresh"
suresh.drink= "Yes"

print(ramesh.name)
print("Drink : ",ramesh.drink)
ramesh.party()
ramesh.beach()
print(suresh.name)
print("Drink : ",suresh.drink)
suresh.party()
suresh.beach()