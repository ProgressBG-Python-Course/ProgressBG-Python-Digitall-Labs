import pdb

def factorial(n):
    pdb.set_trace()

    if n==1:
        return 1
    else:
        return n*factorial(n)

x = 1
print( factorial(5) ) # 120 (5*4*3*2*1)

