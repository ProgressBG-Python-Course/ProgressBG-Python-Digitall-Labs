# standard function definition:
# def sqrt(x):
#     return x**2


# # define sqrt with lambda:
# sqrt = lambda x: x**2;

# print( sqrt(3) )



# def greet():
#     return "Hello, World!"

# greet = lambda: "Hello, World!"

# res = greet()

# print(res)



# ---------------------------- Lambdas in sorting ---------------------------- #
# data = [
#     (1, 'Z'),
#     (3, 'X'),
#     (2, 'Y')
# ]

# def sort_tuple_by_first(t):
#     return t[1]

# print( sorted(data, key=sort_tuple_by_first, reverse=True) )

# print( sorted(data, key=lambda t: t[0], reverse=True) )


# Example
# TASK: sort users in place by age
# users = [
#     {'name': 'Alice', 'age': 30},
#     {'name': 'Bob', 'age': 25},
#     {'name': 'Charlie', 'age': 35}
# ]

# users.sort(key= lambda user:user['age'])

# print(users)


# TASK:
# products = {
#     'apple': 2.50,
#     'beer': 1.2,
#     'bread': 0.90
# }

# sorted_products = sorted(products.items(), key=lambda t:t[1])
# print(sorted_products)
# # print( list(products.items()) )

