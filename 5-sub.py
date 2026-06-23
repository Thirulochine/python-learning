tam=int(input())
eng=int(input())
mat=int(input())
sci=int(input())
ss=int(input())
add=tam+eng+mat+sci+ss
avg=add/5
if(avg<35):
    print("additional class is required")
else:
    print("you are good to go")
