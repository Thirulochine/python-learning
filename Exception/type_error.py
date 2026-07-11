try:
    a=int(input("Enter a : "))
    b=int(input("Enter b : "))
    c=input()
    
    print(c/a)

except ValueError as e:
    print(e)
    
except TypeError as e:
    print("Type Error" ,e)