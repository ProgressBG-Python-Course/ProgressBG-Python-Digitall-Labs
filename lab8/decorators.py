# def stars_decorator(f):
#     def wrapper():
#         print("*" * 50)
#         f()
#         print("*" * 50)

#     return wrapper


# @stars_decorator
# def greet():
#     print("Howdy World!")

# greet = stars_decorator(greet)

# greet()



# def log():
#     print('greet is called')

# def add_stars():
#     print('*'*10)

# def greet(name):
#     log()
#     add_stars()
#     print(f'Hello, {name}')
#     add_stars()

# greet('Ada')

# def log_and_star(f):
#     def wrapper(name):
#         log()
#         add_stars()
#         f(name)
#         add_stars()

#     return wrapper

# @log_and_star
# def greet(name):
#     print(f'Hello, {name}')


# greet('Ada')


# -------------------------- Decorate add with stars ------------------------- #
# def stars_decorator(f):
#     def wrapper(x,y):
#         print('*'*30)
#         res = f(x,y)
#         # print(res)
#         print('*'*30)
#         return res


#     return wrapper


# @stars_decorator
# def add(x,y):
#     return x+y

# # ...

# print( add(2,3) )


# --------------------------- "Universal" decorator -------------------------- #
def stars_decorator(f):
    def wrapper(*args):
        print('*'*30)
        return f(*args)
    return wrapper


@stars_decorator
def add_2(x,y):
    return x+y

@stars_decorator
def add_3(x,y,z):
    return x+y+z


print( add_2(2,3) )
print( add_3(2,3,1) )

