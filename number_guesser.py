---------------------------------------------------------------------------------------------------------------------------------------------------------
# number guesser game using function and random module
import random

def game():
    num = random.randint(1,50)

    while True:
        user_num = int(input("Guess the number: "))
        
        if user_num == num:
            print("You won!!")
            break
        elif user_num < num:
            print("Too low")
        else:
            print("Too high")
    print("Thankyou")

game()
-----------------------------------------------------------------------------------------------------------------------------------------------------------
Output:
Guess the number: 20
Too high
Guess the number: 18
Too high
Guess the number: 12
Too high
Guess the number: 10
Too low
Guess the number: 11
You won!!
Thankyou
---------------------------------------------------------------------------------------------------------------------------------------------------------------
    
