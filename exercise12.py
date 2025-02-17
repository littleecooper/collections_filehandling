# This is a list with all the different types of cheese
cheese = ['Cheddar', 'Stilton', 'Cornish Yarg']

# WHAT IS WRONG WITH THE CURRENT SYNTAX
# This does add it to the list but as three separate items
# The += adds a number to a variable but changes the variable within the process itself
# This is the issue, it adds it as three separate letters as opposed to it being one single item in a list
# cheese += ('Oke')

# ADDING OKE TO THE END OF THE LIST
# created a new variable called new_cheese_list - original list is immutable so, I created the new one to gain the new list
# used the .append string method as this adds the item onto the end of an existing list
# syntax = VARIABLE NAME . STRING METHOD ("THE CHANGE")
new_cheese_list = cheese.append("Oke")
# Printed the new cheese list to see if it works
print(new_cheese_list)

# I printed the variable to see what it looked like in the output with the += variable
print(cheese)

# ADDING TWO ITEMS INTO A LIST USING A SINGLE COMMAND
# created a new variable called "gouda and brie added list"
# used the .extend method to add two new items in a single command line
# have to print off the original list as it will turn into a boolean if you print the new list
# Need the two square brackets to have them as single items
# have to have a comma in the middle to separate the items
gouda_and_brie_added_list = cheese.extend(["Gouda" , "Brie"])
print(cheese)

# QUESTION 2 Why does the first output have 5 and the last have 1
# this has an output of 5 because it is a string
# there are 5 letters in the word 'Hello' so thats why it prints out 5
tup = 'Hello'
print(len(tup))
print(type(tup))

# This one prints out 1 because the comma makes it a tuple which is a collection of elements
# This makes the word 'Hello' a collection of one element and this is why the output is 1
tup = 'Hello',
print(len(tup))
print(type(tup))