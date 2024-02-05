# l = [1,2,3]
# for el in l:
#     print(el)

# # list_iter = l.__iter__()
# list_iter = iter(l)
# print( next(list_iter) )
# print( next(list_iter) )
# print( next(list_iter) )
# print( next(list_iter) )


# -------------------------- Create Custom Iterator: ------------------------- #
# class NumberIterator:
#     def __init__(self, max=5):
#         self.max = max

#     def __next__(self):
#         if self.max>0:
#             self.max-=1
#             return 1
#         else:
#             raise StopIteration

#     def __iter__(self):
#         return self


# my_iter = NumberIterator(max=3)

# print( next(my_iter) )
# print( next(my_iter) )
# print( next(my_iter) )
# print( next(my_iter) )
# print( next(my_iter) )
# print( next(my_iter) )
# print( next(my_iter) )
# print( next(my_iter) )


# for el in my_iter:
#     print(el)


class FibonacciIterator:
    def __init__(self, count=3) -> None:
        self.count = count
        self.prev = 0
        self.next = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.count>0:
            self.count-=1
            value =  self.prev + self.next
            self.prev, self.next = self.next, value
            return value
        else:
            raise StopIteration


for el in FibonacciIterator(10):
    print(el, end=",")


