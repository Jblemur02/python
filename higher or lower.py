import random

print("Welcome to higher or lower.")
print("The objective of the game is to guess if the next number will be greater than theprevious number")
print("You will start with 1000 dollars")

money =  1000
print("Type the number 1 if you think the next number will be higher or 2 if it will be lower.")
pnum = random.randint(0,10)
while(money > 0):
    print("-----------------------------------------------------------------")
    rnum = random.randint(0,10)
    print("The first number is",pnum)
    guess = input("Higher or lower\n")
    while guess != "1" and guess != "2":
        guess = input("1 for higher and 2 for lower")
    unum = int(guess)
    while pnum == rnum:
        pnum = random.randint(0,10)
    
    if unum == 1 and rnum > pnum:
        money += 200
        print("Correct!")
        print("You have ",money," dollars")
        print("The random number was ",rnum)
        pnum = random.randint(0,10)
    elif unum == 2 and rnum < pnum:
        money += 200
        print("Correct!")
        print("You have ",money," dollars")
        print("The random number was ",rnum)
        pnum = random.randint(0,10)
    else:
        money -= 200
        print("Incorrect!")
        print("You have ",money," dollars")
        print("The random number was ",rnum)