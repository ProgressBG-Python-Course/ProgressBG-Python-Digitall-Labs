import sys
import argparse

parser = argparse.ArgumentParser(description='Test')

def add(x,y):
    print(x+y)



parser.add_argument('x',help='int value for x')
parser.add_argument('y',help='int value for y')

args = parser.parse_args()
print(args.x, args.y)

# add(x,y)
