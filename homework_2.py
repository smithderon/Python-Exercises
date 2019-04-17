# 1
# secret = 5
# while secret == 5:
#     guess = int(input("I'm thinking of a number between 1 and 10....what is it?"))
#     if guess == 5:
#         print ("Wow, psychic, huh?")
#         break
#     elif guess != 5:
#         print ("Pathetic, try again.")

#2

# secret = 5
# while secret == 5:
#     guess = int(input("I'm thinking of a number between 1 and 10....what is it?"))
#     if guess == 5:
#         print ("Wow, psychic, huh?")
#         break
#     elif guess <= 5:
#         print ("Too little, try higher.")
#     elif guess >= 5: 
#         print ("Too high, try again.")

#3

# import random 
# secret = random.randint(1, 10)
# while secret == secret:
#     guess = int(input("I'm thinking of a number between 1 and 10....what is it?"))
#     if guess == secret:
#         print ("Wow, psychic, huh?")
#         break
#     elif guess <= secret:
#         print ("Too little, try higher.")
#     elif guess >= secret: 
#         print ("Too high, try again.")

#4 & Bonus

import random 
def game():
    secret = random.randint(1, 10)
    guesses = 4
    while secret == secret and guesses >= 0:
        guess = int(input("I'm thinking of a number between 1 and 10....what is it? "))
        if guess == secret and guesses >= 1:
            print ("Wow, psychic, huh?")
            break
        elif guess <= secret and guesses >= 1:
            print ("Too little, try higher. Oof, you only have %d tries remaining"%(guesses))
            guesses -= 1
        elif guess >= secret and guesses >= 1: 
            print ("Too high, try again. You have %d tries remaining." % (guesses))
            guesses -= 1
        elif guesses == 0:
            maybe = input("""
            Wow, you failed 5 whole times! Game Over!
            Would you like to play again? (Y/N)
            """)
            if maybe == "Y":
                return(game())
            elif maybe == "N":
                print("That's too bad. Have a nice day!")
                break
            break
print(game())