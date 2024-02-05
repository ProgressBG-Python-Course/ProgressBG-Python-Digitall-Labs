# try:
#     user_age = int('ahjahf')
# except:
#     print('Wrong value for user age!')
#     exit(0)
# else:
#     print(user_age)


# print('End')


# try:
#     db.users.insert('Maria')
#     db.users.insert(23)
# except:
#     db.rollback()
# finally:
#     db.disconnect()




# try:
#     print(divide)
#     divider = int('asdhj')
#     result = 10 / divider
# except ZeroDivisionError:
#     print("Divided by zero!")
# except ValueError:
#     print("Incorrect value used in operation.")
# except Exception:
#     print("Upps, something went wrong")
# else:
#     print("Operation successful.")



# try:
#     divider = 0
#     result = 10 / divider
# except Exception as e:
#     print(e)


# ------------------------------ raise exception ----------------------------- #
# int('hdfj')


# def get_user_age():
#     while True:
#         try:
#             age = int(input('Age: '))
#             if 0<age<101:
#                 return age
#             else:
#                 raise Exception(f'{age} is not valid!')
#         except ValueError:
#             print('Wrong value')

#         except Exception as e:
#             print(e)



# user_age = get_user_age()
# print(f'You are: {user_age} old!')




# try:
#     result = 10/0
# except ZeroDivisionError as r:
#     print('Log error: ')
#     raise Exception('...')
# except Exception as e:
#     print(f'######### ERROR: {e}')



# ------------------------ Define Custom Error Classes ----------------------- #
# class InvalidUserAge(Exception):
#     def __init__(self, age):
#         super().__init__(f'Invalid age: {age}')


# def get_user_age():
#     while True:
#         try:
#             age = int(input('Age: '))
#             if 0<age<101:
#                 return age
#             else:
#                 raise InvalidUserAge(age)
#         except ValueError:
#             print('Wrong value')

#         except Exception as e:
#             print(e)

# user_age = get_user_age()
# print(f'You are: {user_age} old!')


# x = Exception()
# # print( x.__dir__() )
# print( dir(x) )


# sum()
