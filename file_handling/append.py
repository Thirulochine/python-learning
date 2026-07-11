file=open("file_handling/fruits.txt","a")   #append
file.write("mango\n")
file.close()

file=open("file_handling/fruits.txt","r+")
print(file.read())
file.close()