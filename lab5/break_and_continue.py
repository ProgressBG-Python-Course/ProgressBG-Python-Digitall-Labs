# ----------------------------------- break ---------------------------------- #
# # Output letters in a string, until 'i' letter is reached:
# words = 'abcdifg'
# for l in words:
#     print(l)
#     if l=='i':
#         break

# ------------------------------ in nested loops ----------------------------- #
# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]

# search_value = 4

# for row in matrix:
#     print(f'Processing row: {row}')

#     for element in row:
#         print(element, end=',')
#         if element == search_value:
#             break  # Breaks out of the inner loop


#     print() # print new line


# while True:
#     user_name = input('Enter a name (>3):')
#     user_name_length = len(user_name)
#     if user_name_length>=3:
#         break

# print(user_name)


# # Switch emulation (Python <3.10):
# # print program menu:
# print("Select an action:")
# print("1. Action 1")
# print("2. Action 3")
# print("3. Action 3")
# print()


# while True:
#     user_choice = int(input("Enter a number [0-4]: "))

#     match user_choice:
#         case 1:
#             print("Action 1 fired!")
#             break
#         case 2:
#             print("Action 2 fired!")
#             break
#         case 3:
#             print("Action 3 fired!")
#             break
#         case _:
#             print('Wrong input!')



# print(user_choice)


# --------------------------------- continue --------------------------------- #
# # Output all consonant letters: (not in 'aiouey')
# words = 'aobcdifg'
# for l in words:
#     if l in 'aiouey':
#         continue
#     print(l)







