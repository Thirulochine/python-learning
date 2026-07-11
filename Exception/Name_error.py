try:
    a=input()
    b=input()
    c=input()
    print(d)

except ValueError as e:
    print(e)
    
except TypeError as e:
    print("Type Error" ,e)
    
except Exception as e:
    print("Something wrong",e)
    