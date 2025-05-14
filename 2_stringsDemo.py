test= "hello\
python\
you\
are\
dynamic"
print(test)
print(type(test))
print(len(test))

test1="""welcome
to
the
world
of
Python"""
print(test1)
print(type(test1))
print(len(test1))

name="Krunal"
age=18
#print(name + "is" + age + "years old!")
print(name + " is " + str(age) + " years old!") # type casting to str
print(name , "is" , age , "years old!") # printing multiple args,default sep=""
print("{} is {} years old".format(name,age))
print("{0} is {1} years old".format(name,age))

print("{}, A computer science portal.".format("StackOverFlow"))
string = "This article is written in {}"
print(string.format("Python"))

#number of placeholder and values must be same
my_string = "{}, is a {}  science portal for {}"
print(my_string.format("StackOverFlow","computer","geeks"))

#indexing
mystring= "Python Basic"
print(mystring[0])
print(mystring[3])
print(mystring[-3])



#Slicing
print(mystring[0:8])
print(mystring[:8])
print(mystring[2:])
print(mystring[2:10:2])
print(mystring[::-1])

str="hello"
print(str)
#str[0]="H"
newstr=str[1:]
print(newstr)
str = "H" + newstr
print(str)

#join()
fname="krunal"
lname="trivedi"
email="a@a.com"
profile="*".join([fname,lname,email])
print(profile)

#upper(),lower(),title()
mixed_case= "PYthOn tRAiniNG"
print(mixed_case.upper())
print(mixed_case.lower())
print(mixed_case.title())

#strip(): without argument
ugly="\n \t Some story to tell "
print(ugly)
stripped = ugly.strip()
print(stripped)

#strip(args)
string="@@@@Geeks for Geeks@@@@"
print(string)
print(string.strip("@"))

#split() : without argument
sentence = "three different words"
words = sentence.split()
print(words)
print(type(words))

#split(args)
secret_data = "1001,0101,0011"
binaries = secret_data.split(",")
print(binaries)

#replace()
doyouknow="Python is my favourite language"
newstring = doyouknow.replace("is","will be")
print(newstring)

ugly_mixed_string = " THiS LOokS BAd "
pretty = ugly_mixed_string.strip().lower().replace("bad","good")
print(pretty)


number1 = input("Enter number :")
print(number1)
print(type(number1))

number2 = int(input("Enter number :"))
print(number2)
print(type(number2))

number3 = eval(input("Enter number :"))
print(number3)
print(type(number3))








