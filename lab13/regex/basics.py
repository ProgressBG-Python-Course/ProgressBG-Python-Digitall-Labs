import re

# # Match any vowel character
# vowels = re.findall(r'[aeiouy]','astroid' );
# non_vowels = re.findall(r'[^aeiouy]','astroi$%$#%$#d' );
# print(vowels)
# print(non_vowels)


# ---------------------------- match white spcces ---------------------------- #
# text = """line1
# line 2
# line 3
# """

# whitespace = re.findall(r'\s', text)
# print(whitespace)


# ---------------------------- Validate user name ---------------------------- #
# 1. Only letters, digits, '_', '-'
# 2. Length: between 3 - 20 symbols
# 3. Must start with letter (1ivan => invalid)

# user_names = """
# ivan1
# ivan_-1

# iv
# 1ivan
# """

# valid_names = re.findall(r'^[a-z][\w-]{3,20}$', user_names, re.MULTILINE|re.IGNORECASE)
# print(valid_names)


# \w\b\W
# --------------------------- Match variables only --------------------------- #
# code = """
# x = 1
# rex = 'usxduis'
# ax = 3
# print(x)
# print('x')
# """

# replaced = re.sub(r'\bx\b$', 'X', code, flags=re.MULTILINE)
# print(replaced)




# # commented regex
# rg = r'''
# ^           # start of
# START
# (.+)        # capture
# END
# $           # end
# '''

# text = """
# STARThjfd
# sdjdshEND
# """

# # TODO: fix
# res = re.findall(rg, text, re.X|re.DOTALL)
# print(res)


# --------------------------------- Capturing -------------------------------- #

# text = """
# ivan:08812331
# maria   :998358
# """

# rg_obj = re.compile(r'^(\w+)\s*:\s*(\d+)$', re.MULTILINE )
# res = rg_obj.findall(text)
# print(res)


# ----------------------------- Match and Search ----------------------------- #
# TODO..
user_name = '!ivan21'
# variant 1
# re.match(r'\w{8,}', user_name, re.IGNORECASE)
# variant 2
regex = re.compile(r'\w{3,}')
m = regex.match(user_name, re.IGNORECASE)
if m:
    print('valid')






