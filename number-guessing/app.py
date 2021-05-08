# Import random module
import random

# Generate number and store in variable
value = random.randint(1,10)

# Start loop
loop = 0
status = 'wrong'

while (status != 'true'):

    guess = int(input("Guess the number: "))

    if (guess != value) and (guess > value):
        loop += 1
        print("Lower...")
    elif (guess != value) and (guess < value):        
        loop += 1
        print("Higher...")
    else:
        print("Correct! It took you " + str(loop) + " tries!") 
        break