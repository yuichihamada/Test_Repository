import traceback
import requests

def catch_response():
  urls = [
    'httpss://google.com',
    'google.com',
    'https://google.coms',
    'https://google.com'
  ]
  exceptions = []
  for url in urls:
    try:
      r = requests.get(url)
    except Exception as e:
      e.add_note('url:{}'.format(url))
      exceptions.append(e)
  if len(exceptions) > 0:
    raise ExceptionGroup('例外発生', exceptions)

try:
  catch_response()
except requests.exceptions.ConnectionError as ce:
  print('Connection Error')
except requests.exceptions.MissingSchema as me:
  print('Missing Schema')
except requests.exceptions.InvalidSchema as ie:
  print('Invalie Schema')
except Exception as e:
  traceback.print_exception