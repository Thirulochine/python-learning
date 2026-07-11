try:
    a=int(input("Enter a number : "))
    
except ValueError as e:
    print("Value Error ",e)