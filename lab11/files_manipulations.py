import os

# fh = open('./data/example.txt')
# # do something with fh
# fh.close()

# read from file
# with open('./data/example.txt','r') as fh:
#     content = fh.read()

#     print(content)

# with open('./data/example.txt','r') as fh:
#     content = fh.readlines()
#     lines = [line.strip() for line in content]
#     print(content)
#     print(lines)

# # best for read line by line
# with open('./data/example.txt','r') as fh:
#     for line in fh:
#         print(line.strip())

# ------------------------------ write in files ------------------------------ #

# with open('./data/example.txt','w') as fh:
#     fh.write("""
# line1
# line2
# line3
# """)


lines = ['line1','line2','line3']

# with open('./data/example.txt','w') as fh:
#     fh.writelines([line+'\n' for line in lines])


# with open('./data/users.txt','w') as fh:
#     pass

# system agnostic:
# eol = os.linesep
# with open('./data/example.txt','w') as fh:
#     fh.writelines([line+eol for line in lines])


# with open('./data/users.txt','w') as fh:
#     pass

