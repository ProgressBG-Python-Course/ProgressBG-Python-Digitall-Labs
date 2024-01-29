# for item in [1,2,3]:
#     print(item)

# for item in range(1,4):
#     print(item)

# print('end')

# ------------------------------ loop over dict ------------------------------ #

# person = {
#     "name": "John",
#     "age": 30,
#     "country": "UK"
# }

# # print( person.keys() )
# # print( person.values() )
# # print( person.items() )

# # for k,v in person.items():
# #     print(f"{k}-{v}")

# for k in person:
#     print(k)

# --------------------- get index and value in for loop: --------------------- #
# colors = ["red", "green", "blue"]

# index = 0
# for color in colors:
#     print(f"{index}: {color}")
#     index+=1

# for index in range(len(colors)):
# #     print(f"{index}: {colors[index]}")

# for index,color in enumerate(colors):
#     print(f"{index}: {color}")

# l = [1,2,3,4,5]
# TASK: write squares of last two elements:
# for el in l[-2:]:
#     print(el**2)

# for idx, el in enumerate(l, -2):
#     print(el**2)


# ----------------------------- Nested for loops: ---------------------------- #
# numbers = [1,2,3]
# word = 'ab'

# for i in numbers:
#     for l in word:
#         print(i, l, end=',')
#     print()

# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]

# for row in matrix:
#     for el in row:
#         print(el, end=',')
#     print()



