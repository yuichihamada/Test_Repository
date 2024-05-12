# 文字列型

fruit = "apple"
print(fruit)
print(type(fruit))

print(fruit * 10)
fruit_10 = fruit * 10
print(fruit_10)

new_fruit = fruit + "banana"
print(new_fruit)

fruit = """apple
orange
grape
"""
print(fruit)

fruit = "banana"
print(fruit[2])
print(fruit[-1])

# encode, decode => bytes[]
byte_fruit = fruit.encode('utf-8')
print(byte_fruit)
print(type(byte_fruit))

str_fruit = byte_fruit.decode('utf-8')
print(str_fruit)
print(type(str_fruit))

# count

msg = 'ABCDEABC'
print(msg.count('ABCD'))
print(msg.count('ABC'))
print(msg.count('ABCDEF'))

# startswith, endswith

print(msg.startswith('ABCD'))
print(msg.startswith('ABDC'))
print(msg.endswith('ABC'))
print(msg.endswith('DBC'))

# strip(両橋), rstrip（右端）, lstrip（左端）

msg = ' ABC '
print(msg)
print(msg.strip())
msg = 'ABCDEFABC'
print(msg.strip('C'))
print(msg.strip('CBA'))
print(msg.rstrip('CBA'))
print(msg.lstrip('CBA'))

# upper, lower, swapcase, replace, capitalize

msg = 'abcABC'
msg_u = msg.upper() #大文字
msg_l = msg.lower() #小文字
msg_s = msg.swapcase() #大文字小文字入れ替え
print(msg_u,msg_l,msg_s)

msg = 'ABCDEABC'
msg_r = msg.replace('ABC', 'FFF')
print(msg_r)
msg_r = msg.replace('ABC', 'FFF', 1)
print(msg_r)

msg = 'hello WoRld'
print(msg.capitalize())

# 文字列の一部取り出し、format、islower、isupper

msg = 'hello, my name is taro'
print(msg[:6])
print(msg[6:])
print(msg[1:10])
print(msg[1:10:2])
print(msg[1:10:3])

print('hello {}'.format('Taro'))
name = 'jiro'
print(f'hello {name}') #3.6以上
print(f'{name=}') #3.8以上

msg = 'apple'
print(msg.islower())
print(msg.isupper())

# find, index, rfind, rindex

msg = 'ABCDEABC'
print(msg.find('ABC'))
print(msg.find('BC'))
print(msg.rfind('ABC'))
print(msg.index('ABC'))
print(msg.rindex('ABC'))

print(msg.find('ABCE')) #存在しない場合は-1を表示
print(msg.index('ABCE')) #存在しない場合はエラーが表示