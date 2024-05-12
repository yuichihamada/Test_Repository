#ジェネレータ関数
def generator(max):
  print('ジェネレータ作成')
  for n in range(max):
    try:
      x = yield n
      print('x = {}'.format(x))
      print('yield実行')
    except ValueError as e:
      print('throwを実行しました')

gen = generator(10)
# n = next(gen)
# print('n = {}'.format(n))
# n = next(gen)
# print('n = {}'.format(n))

# for x in gen:
# print('x = {}'.format(x))

#send
next(gen)
gen.send(100)
gen.send(200)
# gen.throw(ValueError('Invalid Value'))
gen.close()
next(gen)