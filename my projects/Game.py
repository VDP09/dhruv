import random

guess = random.randint(0,100)
def age_guess():
    answer = input ("Is your age " + str(guess) + "?\n")
    return answer

    
name = input("What is your Name?\n")
print ("Hello", name)
guess = random.randint(0,100)

if age_guess().lower() == "yes":
    print ("yay I guessed it")
else:
    print("Come on")
    secondtry = int(input('How far away was I?\n'))
    guess = guess + secondtry 
    if age_guess().lower() == "yes":
        print ("yay I guessed it on my second try!")
    else: 
        print("Come On")
        guess = guess - secondtry
        if age_guess().lower() == "yes":
            print ("yay I guessed it on my third try!")
        else:
            print('you LIED to me!!!')


     