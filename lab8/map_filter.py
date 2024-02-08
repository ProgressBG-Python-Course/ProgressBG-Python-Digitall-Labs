# ---------------------------------- Filter ---------------------------------- #
# filter(function, iterable)

# l = [1,2,3,4,5]
# # evens_l = [el for el in l if el%2==0]

# def evens_filter(el):
#     # print(el)
#     return el%2==0

# # evens_l = filter(evens_filter, l)
# evens_l = filter(lambda el:el%2==0, l)

# print(list(evens_l))


# names = ["Ada", "", "", "Maria"]

# # real_names = filter(lambda name:name!="", names)
# real_names = filter(lambda name:name, names)

# print(list(real_names))


# ------------------------------------ Map ----------------------------------- #
# map(function, iterable, ...)

# l = [1,2,3,4,5]
# square_l = map(lambda el:el**2, l)
# print(list(square_l))


# print( chr(1041) )

# letters = map(chr, range(1040, 1072))
# print( list(letters) )


# map multiple iterables
# l1 = [1,2,3]
# l2 = [4,5,6]

# l = map(lambda x,y: x+y, l1, l2)
# print(list(l))


# ---------------------------------- Reduce ---------------------------------- #
from functools import reduce

# reduce(function, iterable[, initializer])
def reducer(acc,value):
    print(acc, value)
    return acc+1

l = [1,2,3, 1,2,1]


count = reduce( reducer , l, 0)
print(count)
