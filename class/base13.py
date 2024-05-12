#ファイル入力

file_path = 'resources/input.csv'
f = open(file_path, mode='r', encoding='utf-8')

# line = f.read() #中身全体
# print(line)

# lines = f.readlines()
# print(lines)
# for x in lines:
#   print(x.rstrip('\n'))

# line = f.readline()
# while line:
#   print(line.rstrip('\n'))
#   line = f.readline()

while(line := f.readline()):
  print(line.rstrip('\n'))

f.close() #ファイルを閉じれます
# →閉じてないとメモリ食う、他の処理でファイル開けない

#with
with open(file_path, mode='r', encoding='utf-8')as f:
  lines = f.readlines()
  print(lines)

print(f.read())