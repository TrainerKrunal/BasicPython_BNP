import os

print(os.listdir()) #list the content of the directory - return files and directories

os.mkdir("testdir")

print(os.getcwd())

os.chdir("testdir")

print(os.getcwd())

os.mkdir("testdir1")
print(os.listdir())
