# ----------------------- function as dictionary value ----------------------- #
# def foo():
#     print('Foo')


# calc = {
#     'add': lambda x,y:x+y,
#     'sub': lambda x,y:x-y,
#     'foo': foo
# }

# --------------------------- function as argumenet -------------------------- #
# def foo():
#     print('Foo')

# def caller(f, x):
#     if x%2==0:
#         f()


# caller( foo, 3 )


# ------------------------- function as return value ------------------------- #
def foo():
    print('Foo')
    return lambda :print('Hi')



# # f = lambda :print('Hi')
# # print(f)  #?
# f = foo()
# f()

# foo()()



