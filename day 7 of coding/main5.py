# Set-methods in python

s= {2, True, "vivek", 2, 5.9, 44}
s2= {2, False, 5.9, 7, 9}

print(s.union(s2))
print(s.intersection(s2))
print(s.difference(s2))


s2.update(s)
print(s2)


print(s.symmetric_difference(s2))
print(s.issubset(s2))
print(s.issuperset(s2))

s.discard(5.9)
print(s)

# s.remove(5.9)
# print(s)

s.clear()
print(s)

s.add(input("Enter what you want to add in the set: \n"))
print(s)