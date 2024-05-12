#all,any

if all((30 < 10, 10 < 20, 'a' == 'a')): #allは全てTrue
  print('allの中の処理')

if any((10 < 20, 10 < 5, 'a' == 'b')): #anyは一つでもTrue
  print('anyの中の処理')

if not any((20 < 10, 10 < 5, 'a' == 'b')):
  print('not anyの中の処理')