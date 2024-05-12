# #リスト
# list_a = [1,2,3,4]
# list_b = []

# print(list_a)
# print(list_a[1])
# print(list_a[-2])

# list_a = [1,[1,2,'apple'],3,'banana']

# print(list_a[1][2])
# list_a[1][2] = 'lemon'
# print(list_a)
# list_a.reverse()
# print(list_a)

#リストのメソッド

list_a = [1,2,3,4,5]

list_b = list_a[1:4:2]
print(list_b)

# append, extend, insert, clear

list_a.append('apple')
print(list_a)
list_a.extend(['banana','melon'])
print(list_a)
list_a.insert(1,'grape')
print(list_a)
# list_a.clear()
# print(list_a)

#remove,pop,count,index
list_a = [0,1,1,2,2,3,3,3,4]
list_a.remove(3)
print(list_a)
value = list_a.pop()
print(list_a, value)
print(list_a.count(1))
print(list_a.index(1))
print(list_a.index(3))

# copy
print(list_a)
list_b = list_a.copy()
list_b[0] = 'AAAAA'
print(list_a)
print(list_b)

#sort, reverse
list_a = ['banana','apple','lemon','grape']

print(list_a)
# list_a.sort()
list_a = sorted(list_a)
print(list_a)
list_a.reverse()
print(list_a)