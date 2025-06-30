import random

def play_guessing_game():
    """Plays a single round of the number guessing game."""
    hidden = random.randrange(1, 10)
    print("\nI'm thinking of a new number between 1 and 9. Try to guess it!")

    while True:
        try:
            guess = int(input("Please enter your guess: "))
        except ValueError:
            print("Invalid input. Please enter a whole number.")
            continue

        if guess == hidden:
            print(f"Correct! The number was {hidden}. Good Job!")
            break
        elif guess < hidden:
            print("Your guess is too low. Try again!")
        else:
            print("Your guess is too high. Try again!")


print("Welcome to the Endless Guessing Game!")
while True:
    play_guessing_game()

    play_again = input("Do you want to play another round? (yes/no): ").lower()
    if play_again != 'yes':
        print("Thanks for playing! Goodbye!")
        break