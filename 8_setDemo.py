Days={"Monday","TuesDay","Wednesday","Thursday","Friday","Saturday","Sunday"}
print(Days)
print(type(Days))
for item in Days:
    print(item,end=" ")
print()

empty_set=set()
empty_set.add(234)
print(empty_set)

numbers={25,234,553,863}
numbers.discard(1) #removes the item if found, no error if not found
#numbers.remove(1) #it throws the error if item not found
numbers.remove(553)
print(numbers)

numbers.add(25)
print(len(numbers))


emps=["A1","B1","C1"]
emps_set = set(emps)
print("A1" in emps_set)
emp_list = list(emps_set)
print(emp_list)


odd_nums=[23,553,79,91,13,7]
numbers.update(odd_nums)  #update() populates all elements of list, tuple,set to set

print(numbers.pop())
n1 = numbers.copy()
print(n1)
numbers.clear() #empty the set
print(numbers)
