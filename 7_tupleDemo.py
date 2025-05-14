empty_tuple=()
print(empty_tuple)
print(type(empty_tuple))
empIDs="1234","A1B1",46
#empIDs=("1234","A1B1",46) #both are same
print(empIDs)
print(type(empIDs))
print(type(empIDs[1]) is int)
print(empIDs)

name_tuple = tuple("Krunal Trivedi")
print(name_tuple)


names="Krunal Trivedi", #remove the comma and observe the type
print(type(names))
print(names)

#empty_tuple[0]="My Tuple" #cannot modify tuple once initialized

names_list=["John","Mike","Bob","Pat"]
print(type(names_list))

empty_tuple=tuple(names_list)+name_tuple
print(empty_tuple)

for element in empty_tuple:
    print(element,end=" ")
print()

print(empIDs.index(46))
print(len(empIDs))
print(name_tuple.count("r"))
