# This helps us to gain access to the random module
# This  will allow us to use their library of functions within the random module for the lottery program
import random

# created a new variable called lottery numbers
# used the module name of random and then used the randint function
# the randint function helps us to get a random number between a set of integers of our choosing
# I put 1 and 50 in the brackets to indicate the integer range
# printed the lottery numbers in our terminal to see if it worked.
# Randint syntax = MODULE . FUNCTION (START, END)
# lottery_numbers = random.randint(1,50)
# print(lottery_numbers)

# used a for loop
# then used the range function to only have 6 iterations of the loop
# if I did not use range, then I would have an infinite for loop
# used the print function to see the random numbers in the terminal
# used a method from the random module called randint for the program to choose 6 random numbers
# This will show 6 random integers in the terminal
for lottery_numbers in range(6):
    print(random.randint(1,50))

# help()
# used the help function to understand how to import the random module into my python project