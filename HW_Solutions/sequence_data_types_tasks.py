# ---------------------------------- Task 1 ---------------------------------- #
""" DESCRIPTION:
    Write a program which will ask the user to enter 3 names.
	The names, should be stored into a list 'names'.
    Create another list 'sorted_name' which will have names, sorted alphabetically. Do not change the original 'names' list.

    TIP: use list.sort() method to sort a list. Note, that the sort() method works "in-place",
"""


names = []

names.append(input('Enter 1st name: '))
names.append(input('Enter 2d name: '))
names.append(input('Enter 3d name: '))

names_sorted = names[:]
names_sorted.sort()
print('\nOriginally entered names: ', names)
print('Sorted names:', names_sorted)


### EXPECTED OUTPUT:
# Enter 1st name: Maria
# Enter 2d name: Ivan
# Enter 3d name: Asen

# Originally entered names:  ['Maria', 'Ivan', 'Asen']
# Sorted names: ['Asen', 'Ivan', 'Maria']
# ---------------------------------- Task 2 ---------------------------------- #
""" DESCRIPTION:
    Write a program that asks the user to enter a word and then checks if the word is a palindrome.
    A palindrome is a word that reads the same forward and backward, ignoring case.

    Tip: you can use str.lower() to convert a string to lowercase
"""

word = input("Enter a word : ")

is_palindrom = word.lower() == word.lower()[::-1]

# Output
if is_palindrom:
    print(f"The word '{word}' is a palindrome")
else:
    print(f"The word '{word}' is not a palindrome")



### EXPECTED OUTPUT:
# Enter a word : racecar
# The word 'racecar' is a palindrome

# Enter a word : car
# The word 'car' is not a palindrome
