#セット

s = {'a', 'b', 'c', 'd'}
t = {'c', 'd', 'e', 'f'}


u = s | t
# u = s.union(t)

print(u)

u = s & t
# u = s.intersection(t)
print(u)

u = s - t
# u = s.difference(t)
print(u)

u = s ^ t
# u = s.symmetric_difference(t)
print(u)

s |= t
print(s)

# issubset, issuperset, isdisjoint
s = {'apple', 'banana'}
t = {'apple', 'banana', 'lemon'}
u = {'cherry'}

print(s.issubset(t))
print(t.issuperset(s))

print(s.isdisjoint(t))
print(s.isdisjoint(u))



