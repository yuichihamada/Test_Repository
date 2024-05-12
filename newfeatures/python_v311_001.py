# Exception Group

def raise_exceptions():
  exceptions = []
  try:
    msg = 'Hello' + 0
  except TypeError as e:
    e.add_note('Type Errorが発生しました')
    exceptions.append(e)
  try:
    num = 10 / 0 # ZeroDivisionError
  except ZeroDivisionError as e:
    e.add_note('ZeroDivision Errorが発生しました')
    exceptions.append(e)
  if len(exceptions) > 0:
    raise ExceptionGroup('例外発生:', exceptions)

try:
  raise_exceptions()
except *TypeError as te:
  print('Type Errorの場合の処理')
except *ZeroDivisionError as ze:
  print('Zero Divisionの場合の処理')
# except ExceptionGroup as eg:
#   import traceback
#   traceback.print_exception(eg)
#   # print(eg)

# try:
#   raise_exceptions()
# except ZeroDivisionError as e:
#   print('Zero Div 発生')
# except TypeError as e:
#   print('Type Error 発生')