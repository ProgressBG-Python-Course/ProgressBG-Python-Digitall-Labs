# ---------------------------------- Task 1 ---------------------------------- #
""" DESCRIPTION:
Write an EvensIterator class, such that its objects can be used in for loops, iterating over the even numbers in specified [start, end] range (both inclusive).
"""

### YOUR CODE HERE
class EvensRange:
    def __init__(self,start,end):
        self.current = start
        self.end = end
        if not self.current<=self.end:
            raise ValueError('Invalid range')

    def __iter__(self):
        return self

    def __next__(self):
        if self.current>self.end:
            raise StopIteration

        value = self.current if self.current%2==0 else self.current+1
        self.current = value+2
        return value

### TEST:
# for x in EvensRange(1,10):
#     print(x, end=",")

### EXPECTED OUTPUT
# 2,4,6,8,10,


# ---------------------------------- Task 2 ---------------------------------- #
""" DESCRIPTION:
Write a generator function, such that will yield an even number in specified [start, end] range (both inclusive).
"""

### Your code here
def evens_generator(start, end):
    for value in range(start, end+1):
        if value%2==0:
            yield value

### TEST:
# for x in evens_generator(1,10):
#     print(x, end=",")

### EXPECTED OUTPUT
# 2,4,6,8,10,


# ---------------------------------- Task 3 ---------------------------------- #
""" DESCRIPTION:
Define a generator function which will yield all Cyrillic Upper Letters, starting from 'А', to 'Я'
Tip: you can get a letter form its code, using the chr() built-in function, as shown in next examples:
print( chr(1040) )
# 'А''

print( chr(1041) )
# 'Б'

print( chr(1071) )
# 'Я'
"""

### Your code here
def cyrilic_letter_generator():
    for code in range(1040, 1072):
        yield chr(code)

# test:
for l in cyrilic_letter_generator():
    print(l, end=",")

### EXPECTED OUTPUT:
# А,Б,В,Г,Д,Е,Ж,З,И,Й,К,Л,М,Н,О,П,Р,С,Т,У,Ф,Х,Ц,Ч,Ш,Щ,Ъ,Ы,Ь,Э,Ю,Я,