import random
chances = 5
guessNum = random.randint(0:9)
enterNum = input("please enter a number between 0 and 9")

while chances > 5:
    if guessNum == enterNum:
        print("Congrats you win! :D")
    else:
        print("Sorry you lost, The number is" + guessNum)

while chances < 5:
    print("Sorry you lost, The number is" + guessNum)