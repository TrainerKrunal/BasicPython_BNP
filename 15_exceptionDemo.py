def DivideExample(a,b):
    try:
        result = a/b
        print(result)
    except ZeroDivisionError as e:
        print("cannot divide by zero. Details :{}".format(e))
    except TypeError as e:
        print("Invalid Data Types. Details :{}".format(e))


DivideExample(10,2)
DivideExample(20,0) #ZeroDivsionError
DivideExample(20,"a") #TypeError

def open_and_read_file(file_name):
    try:
        file=open(file_name,"r")
        content=file.read()
        print(content)
    except FileNotFoundError as e:
        print(f"Error:{e}")
    finally:
        print("Closing the file (if it was opened)")

open_and_read_file("abc.txt")

def DivideExample(a,b):
    if b<10:
        raise Exception("Value cannot be less than 10")
    return a/b

try:
    print(DivideExample(20,12))
    print(DivideExample(10,2))
    
except Exception as e:
    print("Exception caught in caller : {}".format(e))
    
    

