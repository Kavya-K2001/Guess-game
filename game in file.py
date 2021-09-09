import random
import os
import sys

stage = 1
getname = str(input("Enter the UserName : "))


FilePath = str(os.getcwd())

from pathlib import Path

file1 = Path(FilePath + "\\" + getname + ".txt")

if (file1.exists() == False):

    f1 = open(getname + ".txt", "w")
    f1.write(str(stage - 1))
    f1.close()
else:

    r = open(getname + ".txt", "r")
    read = r.read()
    stage = int(read) + 1



incStage = stage
endStage = 10
chances = 5
low = 1
high = 10

while (stage <= endStage):

    if (stage == incStage):
        t = 0
        x = random.randint(low, high)

        print("________ Stage " + str(stage) + " ________")
        num = int(input("Guess a Number between " + str(low) + " & " + str(high) + " : "))
        while (x != 'n'):
            f = open(getname + ".txt", "w")
            f.write(str(stage))
            f.close()
            if (t < (chances - 1)):
                if num < x:
                    print("Your guess is too low")
                    t = t + 1
                    num = int(input("Guess again : "))
                elif (num > x):
                    print("Your guess is too high")
                    t = t + 1
                    num = int(input("Guess again : "))
                else:
                    print("Your Guess is Correct")
                    t = t + 1
                    stage += 1
                    incStage += 1
                    high += 10
                    break
            else:
                print("Game Over Try again")
                f = open(getname + ".txt", "w")
                f.write(str(stage - 1))
                f.close()
                quit()
                break

print("You completed all the levels successfully")
