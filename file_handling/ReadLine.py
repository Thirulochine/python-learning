file=open("file_handling/fruits.txt","a")   #append
file.write("banana\n")
file.close()

file=open("file_handling/fruits.txt","r+")
print(file.readline())    #only read 1st line
