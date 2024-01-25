# ----------------------------------- Intro ---------------------------------- #
# Immutables : Copy by value:
# x = 5
# copy = x
# x = 3
# print(x,copy)

# Mutable: Copy by reference:
# l = [1,2,3]
# l2 = l
# l[0] = 9

# print(l, l2)


# RAM:
#     x:    3
#     copy: 5
#     l:0x123 => [1,2,3]
#     l2: 0x123

# ------------------------------- Shallow Copy ------------------------------- #
# data = [[1],[2],[3]]

# copy = data[:]
# copy = data.copy()


# RAM:
#      data:
#         0: 0x123: [9],
#         1: 0x122: [2],
#         2: 0x124: [3]]
#      copy:
#         0: 0x123: ,
#         1: 0x122: ,
#         2: 0x124: ]

# data[0] = 9
# print(data, copy)
# [9, [2], [3]] [[1], [2], [3]]

# data[0][0] = 9
# print(data, copy)
# # [[9], [2], [3]] [[9], [2], [3]]


# ------------------------------- Deep Copy ------------------------------- #
# import copy

# data = [[1],[2],[3]]

# deep_copy =copy.deepcopy(data)

# data[0][0] = 9
# print(data, deep_copy)
# [[9], [2], [3]] [[1], [2], [3]]


