from random import randint

def guessthenumber():
    again = "yes"

    while again == "yes":
        min_r = int(input("Enter your minimum value for the game: "))
        max_r = int(input("Enter your maximum value for the game: "))

        number = randint(min_r, max_r)

        print(f"OK, I've thought of a number between {min_r} and {max_r}.\n")
        prompt = "Make a guess: "
        answer = -1
        counter = 0

        while answer != number:
            answer = int(input(prompt))
            counter = counter + 1
            if answer < number:
                print("That's too low. \n")
            elif answer > number:
                print("That's too high. \n")
        print("That was my number. Well done!")
        print(f"You took {counter} guesses.\n")

        again = input("Would you like to play again? (yes / no) ").lower()
        if again.startswith("n"):
            print("Thank you for playing!")
            break

    print("Goodbye!")


guessthenumber()