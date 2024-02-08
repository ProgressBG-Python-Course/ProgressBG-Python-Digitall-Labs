### long way to write even numbers generator
# def even_numbers(end):
#     number = 0

#     for number in range(0,end+1):
#         if number%2==0:
#             yield number

# for number in even_numbers(10):
#     print(number)

# ---------------------- generator comprehensions syntax --------------------- #
# (expression for variable in iterable if condition)

### short way to write even numbers generator
# end = 10
# evens = (number for number in range(0,end+1) if number%2==0)

# for number in evens:
#     print(number)

# 0,2,4,6 8,10

# ------------------------ Example :Process large file ----------------------- #
filename = './example.txt'

# lines generator:
lines = (line for line in open(filename))

# filter (line[0]!='#') and map (line.strip().upper()) generator
non_commment_lines = (
    line.strip().upper() for line in lines if line[0]!='#'
)

print(list(non_commment_lines))
