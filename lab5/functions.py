# def greet( age, user_name='Anonymous', town="London"):
#     # user_name = 'pehso'
#     print('*' * 30)
#     print(f'Hello, {user_name}, you are {age} years old! From {town}')
#     print('*' * 30)


# greet( age=23, town='Sofia') # function call
# greet( user_name='pesho', age=34, town="Plovdiv") # function call


# # RAM:
# #     greet:      0x123: function
# #     user_name:  0x345: 'ada'


# def say_hello(msg, name):
#     print(f"{msg} {name}!")

# say_hello("Hi", name="Maria", )

# ----------------------------------- *args ---------------------------------- #
# def foo(*args, x=9):
#     print(args)

# foo(1)
# foo(1,2, x=3)


# def add(*params):
#     total_sum = 0
#     for p in params:
#         print(p)
#         total_sum += p
#     #TODO: fix bug
#     print(f'{total_sum}:*>30s')

# add( 1,2 )
# add( 1,2,3 )
# add( 1,2,3,4 )


# def greet(*args, first_name="Anonymous"):
#     print(f"Hello, {first_name}!")
#     for other_name in args:
#         print(f"Hello, {other_name}!")

# # Example usage
# greet("Alice", "Bob", "Charlie", "Diana")


# --------------------------------- **kwargs --------------------------------- #
# def foo(x, *args, **kwargs):
#     print(x)
#     if args:
#         print(args)
#     if kwargs:
#         print(kwargs)


# foo(1,2,3, z=9, y=5)


# --------------------------------- unpacking -------------------------------- #
# def foo(p1,p2,p3):
#     print(p1, p2, p3)

# args = [1,2,3]

# # foo(args[0], args[1], args[2])
# foo(*args)

# def foo(p1,p2,p3):
#     print(p1, p2, p3)

# args = {
#     'p1': 1,
#     'p2': 2,
#     'p3': 3
# }

# foo(**args)


# ------------------------------- Return Value ------------------------------- #
def add (x,y):
    print(x,y)
    return x+y
    print()


print( add(2,3) )
print( 2+2 )