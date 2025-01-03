import random

def number_guessing_game():
    number = random.randint(1, 100)  # Generate a random number between 1 and 100
    guesses_left = 7  # Set the initial number of guesses

    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    while guesses_left > 0:
        print(f"\nYou have {guesses_left} guesses left.")
        try:
            guess = int(input("Take a guess: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if guess < number:
            print("Too low!")
        elif guess > number:
            print("Too high!")
        else:
            print(f"\nCongratulations! You guessed the number in {7 - guesses_left} tries.")
            return  # Exit the function after a correct guess

        guesses_left -= 1

    print(f"\nYou ran out of guesses. The number was {number}.")

if __name__ == "__main__":
    number_guessing_game()