import os

# print(f'CWD: {os.getcwd()}')


# contents = os.listdir('./data/')
# print(contents)

### TASK: print filenames in CWD:
# contents = os.listdir()

# for entry in contents:
#     print(entry)
#     if os.path.isfile(entry):
#         print(entry)

# files = [entry for entry in contents if os.path.isfile(entry)]
# dirs = [entry for entry in contents if os.path.isdir(entry)]

# print(files)
# print(dirs)

# ----------------------- List all entries recursivelly ---------------------- #
# def get_all_entries(path=os.getcwd()):
#     entries = []
#     contents = os.listdir(path)
#     for entry in contents:
#         if os.path.isfile(entry):
#             entries.append(entry)
#         else:
#             new_path = os.path.join(path,entry)
#             entries.append(new_path)

#             get_all_entries(new_path)


#     return entries

# print( get_all_entries() )

# for root, dirs, files in os.walk(os.getcwd()):
#     print(list(files))
#     print(list(dirs))


# ---------------------------- mkdir and makedirs ---------------------------- #
# try:
#     os.mkdir('./users/username')
# except FileExistsError as e:
#     print(e)
# except FileNotFoundError as e:
#     print(e)
# except Exception as e:
#     print('Ups, something went wrong')
#     exit(-1)

# try:
#     os.makedirs('./users/username')
# except FileExistsError as e:
#     print(e)
# except Exception as e:
#     print('Ups, something went wrong')
#     exit(-1)


# --------------------- rmdir, removedirs, shutil.rmtree --------------------- #
# try:
#     os.rmdir('./users/username/')
# except FileNotFoundError as e:
#     print(e)
# except OSError as e:
#     print(e)
# except Exception as e:
#     print('Ups, something went wrong')
#     exit(-1)


# try:
#     os.removedirs('./users/username/')
# except FileNotFoundError as e:
#     print(e)
# except OSError as e:
#     print(e)
# except Exception as e:
#     print('Ups, something went wrong')
#     exit(-1)


# import shutil

# try:
#     shutil.rmtree('./users')
# except FileNotFoundError as e:
#     print(e)
# except OSError as e:
#     print(e)
# except Exception as e:
#     print('Ups, something went wrong')
#     exit(-1)
