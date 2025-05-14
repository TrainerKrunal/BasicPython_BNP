
f = open("data.txt","w")
f.write("First line here.\n")
f.write("Second line here. \n")
str_list=["Some more lines...\n","This is Python. \n","I like Python. \n"]
f.writelines(str_list)
f.close()

f=open("data.txt","r")
content = f.read() #reads all content of the file
print(content)

position=f.tell()
print("Position:",position)
f.seek(5)
data_line=f.readline() #reads a current line
print(data_line)
f.close()

f=open("data.txt","r")
data_line = f.readline()
print(data_line,end="")
data_line = f.readline()
print(data_line,end="")
data_line = f.readline()
print(data_line,end="")
f.close()

f=open("data.txt","r")
while True:
    data_line = f.readline()
    print(data_line,end="")
    if len(data_line)==0:
        break
f.close()

import os
os.rename("data.txt","demo.txt")

import shutil
shutil.copy("demo.txt","test.txt")
shutil.copy("demo.txt","fileiofolder")
shutil.move("test.txt","fileiofolder")
os.remove("demo.txt")
        
