s_username="Moni"
s_password="252607"
 
uname=input("Enter user name:")
upass=input("Enter password:")

def validate(uname,upass):
    if uname==s_username and upass==s_password:
        return True
    else:
        return False
    
a=validate(uname,upass)
print(a)