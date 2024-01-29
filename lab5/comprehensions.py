# ---------------------------- List Comprehensions --------------------------- #
### maping:
# input = [1,2,3]
# output = []
# for item in input:
#     output.append(item**2)

# print(output)
# print('~'*30)

# output = [item**2 for item in input ]
# print(output)



# TASK: map input list of letters into list of same letters uppercase
# input = 'abc'
# output_list = []
# for l in input:
#     output_list.append(l.upper())

# output = ''.join(output_list)

# output = ''.join( [l.upper() for l in input] )
# print(output) # ABC

# TASK: map list of symbols to its ascii code
# input = 'abc'

# output = [ord(s) for s in input]
# print(output)
# # print( ord('A') )

### filter
# TASK: from input create output list with evens only:
# input = [1,2,3,4]
# output = []
# for el in input:
#     if el%2==0:
#         output.append(el)

# print(output)

# # new_list = [expression for item in iterable if condition]
# input = [1,2,3,4]
# output = [el for el in input if el%2==0]
# print(output)

# ------------------------- Dictionary Comprehensions ------------------------ #
# new_dict = {key: value for item in iterable if condition}
# eng_bul = {
#     'apple':'ябълка',
#     'orange':'портокал',
#     'banana':'банан'
# }

# bul_eng = {}
# for k,v in eng_bul.items():
#     bul_eng[v] = k

# bul_eng = {v:k for k,v in eng_bul.items()}
# print(bul_eng)

# TASK:  Create new dictionary from student_scores, containing only the items which has values > 4.0

# student_scores = {
#     'ivan':4.5,
#     'maria':5.0,
#     'asen':3.5
# }
# best_students = {k:v for k,v in student_scores.items() if v>4.0}
# print(best_students)

# Creating a dictionary of even numbers and their squares, from a numbers list:
# numbers = [1,2,3,4,5]

# output = {n:n**2 for n in numbers if n%2==0}
# print(output)

# TASK:
keys =   ['a', 'b', 'c']
values = [1,   2,   3]

# d = {k_v:values[idx] for idx,k_v in enumerate(keys)}
# print(d)
# {'a': 1, 'b': 2, 'c': 3}