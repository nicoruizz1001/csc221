from random import randint

def guessthenumber(min_val, max_val):
    number = 100
    again = "yes"

    while again == "yes":
        number = randint(min_val, max_val)
        print("OK, I've thought of a number between {min_val} and {max_val}.\n")
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