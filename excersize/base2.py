# 1~100 3:Fizz, 5:Buzz, 15:FizzBuzz

n = 0
while (n :=n+1) < 101:
  if n % 3 == 0 and n % 5 == 0:
    print(n,':Fizz Buzz')
  elif n % 3 == 0:
    print(n,':Fizz')
  elif n % 5 == 0:
    print(n,':Buzz')
  else:
    print(n)