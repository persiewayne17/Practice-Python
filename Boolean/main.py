#How to use variables, input/output functions, and simple loops
#Introduction to conditional statements
#Guessing Game with a given guess "Wayne"
#this is a test drive two
guess = "Wayne"
guess_word = False
count = 0 
user_name = input("Name of the Player: ")

while True:
    count += 1 
    if count <= 3: 
        user_input = input("Enter the guess word: ")
        if user_input == guess:
            guess_word = True
            break
        else:
            if count == 3:
                print(f"Sorry {user_name}, You are out of guesses")
            else:
                print("Try again!")
    else:
        break

if guess_word:
    print(f"Hurray {user_name}, You have won the game")
else:
    print("You lost the game")