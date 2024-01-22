# x = 1
# l = [1,2]

# RAM:
#     x: 123: 1
#     l: 231:
#         [0]: 1
#         [1]: 2

# l[1]
# l = [1, 'Ada', [1,2]]

# create empty list:
# l1 = list()
# l2 = []

# print( l1 )
# print( l2 )

# if l1:
#     print('Not emptry')

# List demos:
# item1_name = "Milk"
# item1_price = 1.99

# item2_name = "Bread"
# item2_price = 2.49

# item3_name = "Eggs"
# item3_price = 3.59

# item1 = ["Milk", 1.99]
# names = ["Milk", "Bread" ,"Eggs"]

# products = [
#     ["Milk", "Bread" ,"Eggs"],
#     [1.99, 2.49, 3.59]
# ]

# access list elements
# item1 = ["Milk", 1.99]
# print( item1[0] )
# print( item1[1] )
# print( item1[2] )

# products = [
#     ["Milk", "Bread" ,"Eggs"],
#     [1.99, 2.49, 3.59]
# ]

# print( products[0][0] )
# print( products[1][1])

# change list item
# item1 = ["Milk", 1.99]
# item1[1] = 2.50

# print(item1)

# ----------------------------------- Tuple ---------------------------------- #
# birth_date_list = [23, 11, 2000]
# birth_date_tuple = (23, 11, 2000)

# print(birth_date_tuple[2])
# birth_date_tuple[2] = 1999

# x = (2)
# print(type(x))

# y = ()
# print(type(y))

# # create tuple with 1 el:

# z = (2,)
# print(type(z))



# ------------------------- Mutate Tuple's Elements? ------------------------- #
# we can not change immutable tuple item!
# t = (1,2,3)
# t[0] = 9

# we can  change mutable tuple item!
# t = ( [1], [2], 3)
# # l = t[0]
# # print(l[0])
# print( t[0][0] )

# t[0][0] = 9

# print(t)


# -------------------- Converting between list and tuples -------------------- #
# list(), tuple(), range(), str()

# Task: change 14 => 35
# address = ('Bulgaria', 'Sofia', 'Nezabravka str', 14)
# # address[3] = 35
# address_list = list(address)
# address_list[3] = 35

# print(address_list)

# address = list(address)
# address[3] = 35
# print(address)

# l = [1,2]
# t = tuple(l)

# print( id(l[0]) )
# print( id(t[0]) )

# l[0] = 9

# print(l)
# print(t)


# RAM:
#     l:  123: 124,125
#     [0]:124: 1
#     [1]:125: 2
#     t:  125:
#     [0]:127: 1
#     [1]:128: 2

# ----------------------------------- Range ---------------------------------- #
# l = [1,2,3]
# r = range(1,4)

# print(l)
# print(r)

# print(l[2])
# print(r[2])


### Generate renges:
# 3,6,9
# r = range(3,10,3)
# print(list(r))

# r = range(-1,-4,-2)
# print(list(r)) # -1, -3

# r = range(-1,-4)
# print(list(r)) #


# ---------------------------------- Strings --------------------------------- #
# s = 'abc'
# print( s[0] )
# print( list(s) )
# print(s)

# ------------------------- Common Sequence Operation ------------------------ #
### concatenation
# l  = [1,2]
# t = (3,4,5)

# print(l + list(t))

### Membership Testing
# l = range(1,4)
# print(3 in l)
# print(4 in l)
# print(4 not in l)

# print( 'a' in 'abc')


# INDEXING
# l = [1,2,3,4]

# print last element
# print( l[len(l)-1] )
# print( l[-1] )


# print( range(1,4)[-1] )

# SLICING
# l = [1,2,3,4,5]
# get first 2 elements
# l2 = l[0:2:1]
# l2 = l[:2]
# print(l2)
# print(type(l2))

# print( l[2:] )
# print( l[-2:] )
# print( l[-2::-1] )

# print( l[::-1])


#TASK: print word reversed:
# word = 'hello'
# print( word[::-1] )

# TASK: get the last 3 letters:
# word = 'abkjsfkdskcdef'

# print(word[-1:-4:-1]) # fed
# print(word[-3:])

# ------------------------------- List Methods ------------------------------- #
# add element to the end:
# names = []
# for el in range(3):
#     names.append( input('Enter name: ') )

# print(names)

# l = [1,2,3]
# l.append(9)
# print(l)


# l = [1,2,3]
# l.insert(1,9)
# print(l)

# l = [3,1,2]
# # l.sort()
# l.sort(reverse=True)
# print(l)










