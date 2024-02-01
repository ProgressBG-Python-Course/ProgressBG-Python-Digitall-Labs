# -------------------------- Simple Class Definition ------------------------- #
# class Person:
#     def __init__(self, name, age):
#         # set object attributes values:
#         self.name = name
#         self.age = age

#     def greet(self):
#         print(f"Hi there! I'm {self.name}, {self.age} years old!")


# maria = Person("Maria Popova", 25)
# pesho = Person("Pesho", 27)

# maria.greet()
# pesho.greet()

# # RAM:
#     maria:
#             name: Maria
#             age: 23
#     pesho:
#             name: Petar
#             age: 34


# ------------------------------ Class Atributes ----------------------------- #
# class A:
#     count = 0

#     def __init__(self, id):
#         self.id = id
#         A.count+=1

# a1 = A(1)

# a2 = A(2)
# a2.foo = 'Foo'
# a3 = A(3)

# print( a1.__dict__ )
# print( a2.__dict__ )
# print( A.__dict__ )


class A:
    @classmethod
    def class_method(cls):
        print(cls)

    @staticmethod
    def sqrt(x):
        print(x**2)


    def __init__(self, id):
        # self = a1
        self.id = A.sqrt(id)


    # instance methods
    def get_id(self):
        # self = a1
        return self.id


    def test(self, obj):
        print(self)
        print(obj)
        print( self==obj)


a1 = A(1)
a2 = A(2)

a1.test(a1)
A.class_method()












