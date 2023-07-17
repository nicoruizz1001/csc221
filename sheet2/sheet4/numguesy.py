from random import randint

def guessing_game():
    play_again = True

    print("Welcome to the Guessing Game!")
    print("I will pick a number between 1 and 100. Can you guess it?")
    print("Let's get started!")

    while play_again:
        number = randint(1, 100)
        guess = None
        attempts = 0

        while guess != number:
            try:
                guess = int(input("Enter your guess: "))
            except ValueError:
                print("Invalid input. Please enter a valid number.")
                continue

            attempts += 1

            if guess < number:
                print("Too low! Try again.")
            elif guess > number:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You guessed it right in {attempts} attempts.")

        play_again = input("Do you want to play again? (yes/no) ").lower().startswith("y")

    print("Thanks for playing!")

guessing_game()