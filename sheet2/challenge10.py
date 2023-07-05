from random import randint
right = 0 
for x in range (10):
    num1 = randint(1,20)
    num2 = randint(1,20)
    question = "What is " + str(num1) + " times " + str(num2) + " ?"
    answer = int(input(question))
    product = num1 * num2
    if answer == product:
        right = right + 1 
        print("You are correct")
    else:
           print("You are wrong, the correct answer is " + str(product) + ' ' )
print("I asked you 10 questions.  You got " + str(right) + " of them right.")
print("Well done!") 
     
                        
