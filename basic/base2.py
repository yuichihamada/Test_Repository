#変数の応用

animal ='dog'
動物 = 'cat'
print(動物)

# 定数

LEGAL_AGE = 18 #定数は大文字で！
age = 18

if age < LEGAL_AGE: #ageがLEGAL_AGEより小さい時に処理を実行
  print('未成年')
else:
  print('成人')

# format分
print(f'age = {age}') #3.6
print(f'{age=}') #3.8