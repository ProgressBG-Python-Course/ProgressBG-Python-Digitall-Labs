from collections.abc import Iterable


class Person(object):
    def __init__(self, name) -> None:
        self.name = name

    def __dir__(self) -> Iterable[str]:
        return ['name']

# p1 = Person('Ada')
# print( dir(p1) )
# print( p1.__dir__() )

# print( dir(2) )


# print( type(p1) )
# print( type(2) )


# def create_class():
#     Employee = type('Employee', (Person,), dict())
#     pesho = Employee('Pesho')
#     print(type(pesho))


# p1 = Person('Ada')
# if hasattr(p1, 'age'):
#     print( p1.age )
# else:
#     print('No such attribute')

# if hasattr(p1, 'name'):
#     print( getattr(p1, 'na'+'me') )

# # p1.age = 23
# setattr(p1, 'age', 23)
# print(p1.age)

# def add(x,y):
#     if isinstance(x, int) and isinstance(x, int):
#         print(x+y)
#     else:
#         print('x and y are not integers!')


# add('3', '4')


# ------------------------------ inspect module ----------------------------- #
# import inspect

# def foo():
#   func_name = inspect.stack()[0][3]
#   caller_name = inspect.stack()[1][3]
#   print(f"I'm {func_name}.\n{caller_name} called me!")

# def bar(f):
#   f()

# bar(foo)