
def check_size(size: str):
  match size:
    case 'L' | 'XL':
      # print('Lサイズです')
      print('大きめのサイズです')
    case 'M':
      print('Mサイズです')
    case 'S':
      print('Sサイズです')
    case _:
      print('このサイズは存在しません')
  
  print('サイズチェック完了しました')
    
check_size('L')
check_size('P')
check_size('XL')


#ガード
def check_size_price(size: str, price: int):
  match size:
    case 'L' if all([price > 0, price < 2000]):
      return 'Lサイズです'
    case 'M' if price > 0:
      return 'Mサイズです'
    case _:
      return 'サイズと価格の指定が誤っています'


print(check_size_price('L', 3000))
print(check_size_price('M', 100))
print(check_size_price('M', -200))