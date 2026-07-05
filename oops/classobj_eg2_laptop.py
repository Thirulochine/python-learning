class Laptop:
    price=0
    range=""
    ram=""
    
dell=Laptop()
hp=Laptop()
lenovo=Laptop()

dell.price= 50000
dell.range= "High"
dell.ram= "16GB"

hp.price= 40000
hp.range= "Medium"
hp.ram= "8GB"

lenovo.price= 30000
lenovo.range= "Low"
lenovo.ram= "4GB"

print("Dell Laptop Price : ",dell.price)
print("Dell Laptop Range : ",dell.range)
print("Dell Laptop RAM : ",dell.ram)

print("\n")
print("HP Laptop Price : ",hp.price)
print("HP Laptop Range : ",hp.range)
print("HP Laptop RAM : ",hp.ram)

print("\n")
print("Lenovo Laptop Price : ",lenovo.price)
print("Lenovo Laptop Range : ",lenovo.range)
print("Lenovo Laptop RAM : ",lenovo.ram)
