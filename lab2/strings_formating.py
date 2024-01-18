# ----------------------------- Escape Sequences ----------------------------- #
# print( 'hi I\'m iva' )
# print( "hi I'm iva" )

# print("""
# line1
# line2""")

# print('line1\nline2')

# print('a\tb')
# print('x\\y')

# ------------------------------ print function ------------------------------ #
# print(*objects, sep=' ', end='\n')
# print(1,2, sep=',')
# print(3, end=" ")
# print(4)

# ------------------------------ input function ------------------------------ #
# user_name = input('Enter your name:')
# print(user_name)

# x = input()
# x_int = int(x)

# print( type(x) )
# print( type(x_int) )

# x = int(input('x='))
# y = int(input('y='))

# print('x+y=',x+y)

# --------------------------------- f-string --------------------------------- #
# x = 23
# print( x )
# print( f'{x}' )


# user_name = 'Ada'
# user_age = 23

# print('Hello, ' + user_name + '! You are ' + str(user_age) + ' years old.')
# print(f'Hello, {user_name}! You are {user_age} years old.')


# ---------------------------- formating f-strings --------------------------- #
# f'{value:format_spec}'
# print(f'{5:.2f}')

# x = 5.126456
# print(f'x={x:.3f}')

# x = 12_345
# print(f'{x:,.2f}')

# accuracy = 0.95678
# print(f"Accuracy: {accuracy:.2%}")

# x = 5
# print(f'|{x:>10}|')
# print(f'|{x:<10}|')
# print(f'|{x:^10}|')

# print(f'|{x:~>10}|')
# print(f'|{x:~<10}|')
# print(f'|{x:~^10}|')

# x = 5
# print(f'|{x:0>3}|')
# print(f'|{x:03d}|')

# ----------------------------------- Task: ---------------------------------- #
# print next table with row width = 23
# |==========|==========|
# |         1|1         |
# |==========|==========|


# print first line:
# # print('|==========|==========|')
# print(f'|{'='*10}|{'='*10}|')

# width = 23
# output = ''
# output += f'|{'|':=^{width-2}}|\n'
# output += f'|{'1|1':^{width-2}}|\n'
# output += f'|{'|':=^{width-2}}|'

# print(output)



# ---------- Formating with str.format() method (or oldest'%' style) --------- #
### oldest'%' style

# f'{value:format_spec}'
# print(f'{5:.2f}')

# "format_string" % (values_tuple)
# output = ("%.2f") % (5.126456)
# print(output)

# print(("%.2f") % (5.126456))



### str.format()

# print('x={} and y = {}'.format(1+1,2))
# print(f'x={1+1} and y = {2}')










