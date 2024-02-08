# class SimpleIterator:
#     def __init__(self):
#         self.value = 0
#     def __iter__(self):
#         return self
#     def __next__(self):
#         if self.value>=3:
#             raise StopIteration
#         else:
#             self.value+=1
#             return self.value


# for number in SimpleIterator():
#     print(number)


# def simple_generator():
#     yield 1
#     print('yield 1')
#     yield 2
#     print('yield 2')
#     yield 3
#     print('yield 3')

# for number in simple_generator():
#     print(number)

# #1
# # yield 1


# numbers = simple_generator()
# print(next(numbers))
# print(next(numbers))
# print(next(numbers))

# ---------------------------- Fibonacci Generator --------------------------- #
# class FibonacciIterator:
#     def __init__(self, count=3) -> None:
#         self.count = count
#         self.prev = 0
#         self.next = 1

#     def __iter__(self):
#         return self

#     def __next__(self):
#         if self.count>0:
#             self.count-=1
#             value =  self.prev
#             self.prev, self.next = self.next, self.next+value
#             return value
#         else:
#             raise StopIteration


# def fibonacci_generator(count):
#     prev = 0
#     next = 1
#     while count>0:
#         count-=1
#         value =  prev
#         prev, next = next, next+value
#         yield value


# for number in fibonacci_generator(10):
#     print(number, end=",")


# fibonacci = FibonacciIterator(10)
# for el in fibonacci:
#     print(el, end=",")

# ------------------ Example - nested list flatten generator ----------------- #
# def flatten(nested):
#     """Flattens a nested list into a single generator of elements."""
#     for sublist in nested:
#         for element in sublist:
#             yield element

# nested = [[1, 2], [3, 4], [5]]


# for number in flatten(nested):
#     print(number)


# ---------------------- Naive Cyrillic names generator: --------------------- #

from random import randint

def cyrillic_names_generator(count=5, min_length = 3, max_length = 8 ):
    """Naively generates Cyrillic "names" with given length"""
    def _gen_random_vowel():
        idx = randint(0, len(vowels)-1)
        return vowels[idx]

    def _gen_random_consonant():
        # we need only consonant, so loop until one is found
        while True:
            # code 1072 in unicode is for 'a' (CYRILLIC SMALL LETTER A)
            letter = chr(randint(1072, 1103))

            if letter not in vowels:
                return letter

    def _gen_random_name():
        name_length = randint(min_length, max_length)
        # generate list of alternating vowels and consonants
        name_letters = [
            _gen_random_vowel() if i%2 else _gen_random_consonant()
                for i in range(name_length)
        ]
        return "".join(name_letters).capitalize()

    vowels = ["а","о","е","и","ю","я"]

    for c in range(count):
        yield _gen_random_name()


# generate 10 Cyrillic "names":
for name in cyrillic_names_generator(count=10):
    print(name, end=",")


