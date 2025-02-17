import random
# Import the random module

# generates 6 unique random numbers between 1 and 50
lotto_numbers = random.sample(range(1, 51), 6)
# 'range(1, 51)' creates a list of numbers starting from 1 and going up to 50 (but not 51)
# the 6 in a separate bracket means 6 random no.s
# .sample allows us to not pick the same name twice



# displays the lottery numbers
print("Your lottery numbers are:", lotto_numbers)

