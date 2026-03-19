a,b = map(int, input().split())

result = 0

if b >= a - 1:
  result = a + (a-1)
  print(result)
else:
  result = (b + 1) + b
  print(result)