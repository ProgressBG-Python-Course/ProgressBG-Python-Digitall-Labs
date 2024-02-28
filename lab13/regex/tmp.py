# s1 = 'a\tb'
# s2 = r'a\tb'

# print(s1)
# print(s2)

import re

rg = r'[aeiouy]+[a-z]'

text= 'AZ aZ'

res = re.findall(rg, text)
print(res)