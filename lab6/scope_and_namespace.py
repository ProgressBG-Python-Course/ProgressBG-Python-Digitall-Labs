# # Example for local and global scope:
# x = 1

# def foo():
#     x = 2
#     print(f'x in foo: {x}')

# foo()
# print(f'x in global: {x}')

# # NAMESPACES:
# # global  = {
# #       x: 1
# #     foo: (function)
# # }

# # foo = {
# #     x = 2
# # }


# # using locals() and globals()
# x = 1

# def foo(x):
#     y = 2
#     print( f'foo: {locals()}' )

# def bar():
#     x = 5
#     print( f'bar: {locals()}' )


# # foo(9)   # {'x': 9, 'y': 2}
# # bar()    # {x=5}

# # print( f'gloabls: {globals()}')

# print( x )
# print( __file__ )



# ---------------------------------- Example --------------------------------- #

# def foo():
#     def bar():
#         print(f'bar x: {x}')

#     bar()
#     print(f'foo x: {x}')


# x = 3

# foo()

# print(f'global x: {x}')

# # OUTPUT:
# bar x: 1
# foo x: 1
# global x: 3


# ------------------------------ global keyworod ----------------------------- #
# def outer():
#     x=2

#     def inner():
#         global x
#         x = 3 # we change the global x
#         print(f'x = {x} in inner')

#     inner()
#     print(f'x = {x} in outer')

# x = 1
# outer()
# print(f'x = {x} in global')


#OUTPUT:
# x = 3 in inner
# x = 2 in outer
# x = 3 in global


# ---------------------------------- Example --------------------------------- #
# def increment_count():
#     global count
#     count+=1


# count = 1

# increment_count()
# print( count )





