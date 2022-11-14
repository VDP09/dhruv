import random

name = input("What is your Name?\n")
print ("Hello", name)
guess = random.randint(0,100)
answer = input ("Is your age " + str(guess) + "\n")
if answer == "yes":
    print ("yay I guessed it")
else:
     print("Come on")
