
def my_first_function():
    print("Hello World!")

my_first_function() #calling function

print(my_first_function) #passing function reference


def greet_us(name1,name2):
    print("Hello {} and {}".format(name1,name2))


greet_us("John","Krunal")

def strip_and_lowercase(original):
    modified = original.strip().lower()
    return modified

uggly_string="  MIXed cASe "
pretty=strip_and_lowercase(uggly_string)
print(pretty)

def simple_interest(p,r,t):
    return (p*r*t)/100
p = float(input("Enter the principle amount:"))
r = float(input("Enter the rate of interest:"))
t=  float(input("Enter the time in years:"))
print(simple_interest(p,r,t))


def create_person_info(name,age,job=None,salary=300):
    info={"personname":name,"personage":age,"personsalary":salary}

    if job is not None:
        info["personjob"]=job

    return info

person1=create_person_info("John",82)
print(person1)
person2=create_person_info("Lisa",65,"hacker",1000)
print(person2)

def my_fancy_calculation(first,second,third):
    return first+second-third

print(my_fancy_calculation(10,12,5))
print(my_fancy_calculation(first=10,second=12,third=5))
print(my_fancy_calculation(second=10,third=12,first=5))


def mydata(*names):
    print(type(names))
    for item in names:
        print(item)
mydata("John","Mike","Pat")
mydata()
mydata(10,20)
mydata(True)
mydata([1,2],[3,4])




