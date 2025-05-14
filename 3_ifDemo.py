
number = int(input("Enter an integer :"))
if (number%2==0):
    print("{0} is an even number".format(number))
else:
    print("{0} is an odd number".format(number))

print("Done")

number=25
guess = int(input("Enter an integer:"))
if guess == number:
   print("you won")
elif guess < number:
    print("The actual number is higher than that")
else:
    print("The actual number is lower than that")
print("Done")
