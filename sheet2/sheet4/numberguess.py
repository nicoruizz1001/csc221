from random import randint

number = 1000
again = "yes"

while again == "yes":
    number = randint(1, top)
    print(f"OK, I've thought of a number between 1 and 1000.\n")
    prompt = "Make a guess: "
    answer = -1
    counter = 0
    while answer != number:
        answer = int(input(prompt))
        counter = counter + 1
        if answer < number:
            print("That's too low. \n")
        elif answer > number:
            print("That's too high dude. \n")
    print("That was my  number. Well done!")
    print(f'\nYou took {counter} guesses. ')

    again = input("Would you to play again? (yes / nope)") .lower().startswith("y")
print(" bye!")