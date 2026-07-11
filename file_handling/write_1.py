f=open("file_handling/fruits.txt","w")
f.write("banana\n")
f.write("pineapple")
f.close()

f=open("file_handling/fruits.txt","r+")  #r+ allows read and write
print(f.read())