salary=int(input("salary:"))
age=int(input("age:"))
if(salary>=20000 or age<=25):
    loan=int(input())
    if(loan<=50000):
        print("Eligible for loan")
    else:
        print("Max loan amount is 50000")
else:
    print("Not eligible for loan")