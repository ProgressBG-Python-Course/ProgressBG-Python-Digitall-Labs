# ------------------------------------ if ------------------------------------ #
# if 0:
#     print(1)
#     print(2)

# print(3)

# Taks: print 'Even' if x is even:
# x = 6
# if x%2==0:
#     print('Even')

# # Taks: print 'Odd' if x is odd:
# if x%2:
#     print('Odd') #

# ---------------------------------- if-else --------------------------------- #

# Taks: print 'Even' if x is even, print 'Odd' if x is odd:
# x = 6

# if x%2==0:
#     print('Even')
# else:
#     print('odd')

# print('hi')

# ------------------------------- if-elif-else ------------------------------- #

# Taks: print 'Even' if x is even, print 'Odd' if x is odd. Print 'Zero' if x ==0
x = 6

### Worst variant
# if x==0:
#     print('Zero')
# else:
#     if x%2==0:
#         print('Even')
#     else:
#         print('odd')

### Best variant
# if x==0:
#     print('Zero')
# elif x%2==0:
#     print('Even')
# else:
#     print('odd')

# -------------------------- Conditional Expression -------------------------- #
#task: if user is adult, status='adult', else status='child'

# user_age = 19
# status = ""
# if user_age>=18:
#     status='adult'
# else:
#     status='child'

# Pythonic way:
# status = 'adult' if user_age>=18 else 'child'
# print(status)


# -------------------------- Statement vs Expression ------------------------- #
# x = 1 # statement

# print( y:=2 )
# print( x=1 )

# print(y)

# ---------------------------- Operator Precedence --------------------------- #
# x = 0
# y =- 1

# print( x and y + 2 )
# print( x and (y + 2) )
# print( (x and y) + 2 )


