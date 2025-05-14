myemptylist=[]
print(myemptylist)
print(type(myemptylist))

list_ints=[1,2,6,7]
list_misc=[1,0.2,5,"Python","is","fun"]
print(len(list_ints))
print(len(list_misc))
intSeq = list(range(1,10))
print(intSeq)

#access and modify the list elements
intSeq[2]=111
print(intSeq)

#airthmetic operation on list is not possible directly
print(list_ints*2) #repetition

#we need to grab the list element based on index OR we use for loop
print(list_misc[2]*2) #grabbing the list element by index

for item in list_ints:
    print(item*2)

#2D List
list1=[[12,13],[11,10],[13,15]]
print(list1[0])
print(list1[0][1])
print(list1[1][1])
print(list1[2][0])
print(list1[0:2]) #List Slicing : list1[start:stop]

del intSeq[0]
print(intSeq)


languages=["Java","C++","Go","Python"]
if "Java" in languages:
    languages.remove("Java")
    print(languages)

if 6 not in [1,2,3,7]:
    print("6 is not present")

original=[1,2,3]
modified=original
modified[0]=99
print(original,modified)

#copy()
original=[1,2,3]
modified=original.copy()
modified[0]=99
print(original,modified)

#append(),insert()
mylist=[1]
print(mylist)
mylist.append("Bread") #adds the item at the end
print(mylist)
mylist.insert(0,"Butter") #adds the item at given index
print(mylist)
mylist.insert(300,"Chocolate") #works like append when try to add item at non-existent index
print(mylist)
print(mylist.index("Chocolate"))

#sort()
numbers = [8,1,6,5,10]
print(numbers)
numbers.sort()
print(numbers)
numbers.sort(reverse=True)
print(numbers)

words=["this","a","is","b"]
words.sort()
print(words)

numbers1=[8,1,6,5,10]
newnumbers1=sorted(numbers1)
print(numbers1,newnumbers1)

#reverse()
my_list=["a","b","z"]
my_list.reverse()
print(my_list)





