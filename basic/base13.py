# セット

set_a = {'a', 'b', 'c', 'd', 'a', 12}
print(set_a)
print('e' in set_a)
print('a' in set_a)
print('a' not in set_a)

print(len(set_a))

# add , remove , discard , pop, clear

set_a.add('A')
print(set_a)

set_a.remove('a')
print(set_a)

set_a.discard(12)
print(set_a)

val = set_a.pop()
print(val, set_a)

set_a.clear()
print(set_a)
