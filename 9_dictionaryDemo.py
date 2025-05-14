empty_dict={}
print(type(empty_dict))

print(empty_dict)

userDetails={"name":"Krunal","age":38}
print(userDetails)

#add new entries
userDetails["loc"]="Mumbai"
print(userDetails)

'''
userDetails={}
for i in range(3):
    key=input("Enter key:")
    value=input("Enter value:")
    userDetails[key]=value
print(userDetails)
'''

userDetails={"name":"Krunal","age":38,"loc":"Mumbai"}
print(userDetails)
userDetails["loc"]="Chennai" #if key exists, it will be updated with new value
print(userDetails)

userDetails["phone"]="9998472789" #if key doesnot exist,it will add new key and value
print(userDetails)

#values()
print(userDetails.values())

#keys()
for item in userDetails.keys():
    print(item," : ",userDetails[item])

#items(): returns key and value both
for key,value in userDetails.items():
    print("{}:{}".format(key,value))

#get()
print(userDetails.get("phone1","Phone key doesn't exists"))

del userDetails["phone"]
print(userDetails)

userDetails.clear()
print(userDetails)





