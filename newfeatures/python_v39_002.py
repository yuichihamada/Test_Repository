# removeprefix, removesuffix
msg = 'Hello World, Hello'
msg2 = msg.removeprefix('He')
#接頭語の指定文字が削除
msg3 = msg.replace('He', ' ')
#文章中の文字が変換

print(msg2)
# llo World

print(msg3)

msg4 = msg.removesuffix('llo')

print(msg4)