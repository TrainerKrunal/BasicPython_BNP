for item in "Python":
    print(item.upper())


for item in range(1,11):
    print(item*2,end=" ")

print()
for i in range(10,0,-1):
    if i==4:
        break #breaks the loop
    elif i==9:
        continue #skip the current value and continue with the next value
    print(i)


for n in range(10):
    print(n,end=" ")

print()
num=7
how_many=5    #(7,36,7)
for n in range(num,num*how_many+1,num):
    print(n)
