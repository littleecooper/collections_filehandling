# question 1:
cheese = ['Cheddar', 'Stilton', 'Cornish Yarg']
# cheese += 'Oke'
# += on a string adds each character separately
print(cheese)
# += 'Oke' treats 'Oke' as an iterable (a string)
# this  means it appends each character ('O', 'k', 'e') individually to the list.

# append is used to add an element to the end of a list
# append adds a single element at the end of the list
cheese.append('Oke')
print(cheese)

# extend is used to add more than one item at once
cheese.extend(['Halloumi', 'Edam'])
print(cheese)

# question 2

tup = 'Hello'  # this is a string, NOT tuple
print(len(tup))  # Prints 5= counts characters of 'Hello'
# len(tup) returns the number of characters in the string, which is 5 ('H', 'e', 'l', 'l', 'o').

tup = 'Hello',  # The comma makes this a tuple
print(len(tup))  # Prints 1= counts how many elements
# a tuple is an ordered, immutable (can't be changed), collection of elements