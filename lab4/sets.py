# l1 = [1,2,1,3,2,5,3]
# l2 = list( set([1,2,1,3,2,5,3]) )
# print(l2)

s1 = {1,2,3,4}
s2 = {2,3,7}


print( s1.union(s2) )
print( s2.union(s1) )

print( s1.intersection(s2))
print( s2.intersection(s1))

print(s1.difference(s2))
print(s2.difference(s1))


print(s1.symmetric_difference(s2))
print(s2.symmetric_difference(s1))

# ---------------------------------- fhdjfd ---------------------------------- #