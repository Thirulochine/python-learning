s1={1, 2, 3, 4, 5}
s2={4, 5, 6, 7, 8}
print("set 1:", s1)
print("set 2:", s2)
print("union of set 1 and set 2:", s1.union(s2))
print("intersection of set 1 and set 2:", s1.intersection(s2))  
print("difference of set 1 and set 2:", s1.difference(s2))
print("symmetric difference of set 1 and set 2:", s1.symmetric_difference(s2))
print("is set 1 a subset of set 2:", s1.issubset(s2))