import random

def guess_the_number():
    number_to_guess = random.randint(1, 100)
    attempts = 7

    print("I'm thinking of a number between 1 and 100.")
    print(f"You have {attempts} attempts to guess it!")

    while attempts > 0:
        try:
            guess = int(input("Enter your guess: "))
        except ValueError:
            print("Please enter a valid integer.")
            continue

        if guess == number_to_guess:
            print("🎉 Correct! You guessed the number!")
            break
        elif guess < number_to_guess:
            print("Too low!")
        else:
            print("Too high!")

        attempts -= 1
        print(f"Attempts left: {attempts}")

    else:
        print(f"Sorry, you're out of attempts. The number was {number_to_guess}.")

# Run the game
guess_the_number()
