x=1
while x <6:
    print(x)
    x+=1


number=25
running=True
while running:
    guess = int(input("Enter positive integer :"))
    if guess==number:
        print("You win!")
        running=False
    elif guess==0:
        break
    elif guess<number:
        print("The actual number is higher than that")
    else:
        print("The actual number is lower than that")
else:
    print("Game over")
