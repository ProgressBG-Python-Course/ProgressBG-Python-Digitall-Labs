# ----------------------------------- intro ---------------------------------- #
# l = [1,2,3]
# d = {
#     'a':1,
#     'b':2,
#     'c':3
# }
# # RAM:
# #      l:
# #         0: 0x123: 1,
# #         1: 0x122: 2,
# #         2: 0x124: 3

# #       d:
# #         'a': 0x123: 1,
# #         'b': 0x122: 2,
# #         'c': 0x124: 3,


# print(l[0])
# print(d['a'])


# --------------------------------- Examples  -------------------------------- #
# user_data_list = ['Maria', 'Ivanova', 23]
# user_data_dict = {
#     'surname': 'Ivanova',
#     'age': 23,
#     'first_name': 'Maria'
# }

# # print(user_data_list[1])
# # print(user_data_dict['surname'])

# print(user_data_dict)

# d = {
#     ('name', 'age'):'Maria',
#     ('name', 'age'):'Ivan'
# }

# print(d[('name', 'age')])

# change item:
# user_data_list[0] = 'Ada'
# user_data_dict['first_name'] = 'Ada'

# print(user_data_list)
# print(user_data_dict)


# l = [1,2,3]
# l[3] = 9

# print(l)

# # add item :
# d = {'a':1, 'b':2, 'c':3}
# d['d'] = 4
# print(d)

# ## remove item:
# d = {'a':1, 'b':2, 'c':3}
# # del d['d']
# value = d.pop('f',None)
# print(d)
# print(value)


# l = [
#     [1,2]
# ]

# d = {
#     'a':{
#         'a':1
#     }
# }

# print( d['a']['a'] )


# get keys:
# d = {'a':1, 'b':2, 'c':3}

# keys_view = d.keys()
# values_view = d.values()

# keys_list = list(keys_view)
# values_list = list(values_view)

# d.pop('b')

# print(keys_view)    # view{['a', 'c']}
# print(keys_list)    # ['a', 'b', 'c']

# # get items:
# d = {'a':1, 'b':2, 'c':3}
# items = list(d.items())
# print(items)


# print( items[1][0] ) # 'b'
# print( items[1][1] ) # 2



# prices = {
#     "apples": 2.50,
#     "oranges": 2.43,
#     "bananas": 3.50
# }

# key = "oranges"
# print( prices[key])
# prices[key] = prices[key] + 2

# for key in prices.keys():
#     prices[key]+=2

# for key in prices:
#     prices[key]+=2


# for value in prices.values():
#     value+=2

# for k,v in prices.items():
#     print(f'{k}={v}')

# k,v = ("apples", 2.50)
# print(k,v)

# week_days_map = {
#     'mon': 0,
#     'tue': 1,
#     'wed': 2,
#     'thu': 3,
#     'fri': 4,
#     'sat': 5,
#     'sun': 6
# }

# day = 'wed'
# print( week_days_map[day])








