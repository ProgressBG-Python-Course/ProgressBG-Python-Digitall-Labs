# ---------------------------------- Task 1 ---------------------------------- #
""" DESCRIPTION:
    Write a program which will ask the user to enter 3 names.
	The names, should be stored into a list 'names'.
    Create another list 'sorted_name' which will have names, sorted alphabetically. Do not change the original 'names' list.

    TIP: use list.sort() method to sort a list. Note, that the sort() method works "in-place",
"""

### Your code here

names = []

for _ in range(3):
    names.append( input('Enter a word:'))


sorted_name = sorted( names )
print(names)
print(sorted_name)



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

# ### Your code here

# print('Enter a word')
# word = input('Enter a word: ')
# reversed_word = word[::-1]

# if word.lower().replace(' ','') == reversed_word.lower().replace(' ',''):
#     print(f"The word '{word}' is a palindrome.")
# else:
#     print(f"The word '{word}' is not a palindrome.")

# ### EXPECTED OUTPUT:
# # Enter a word : Racecar
# # The word 'Racecar' is a palindrome

# # Enter a word : car
# # The word 'car' is not a palindrome