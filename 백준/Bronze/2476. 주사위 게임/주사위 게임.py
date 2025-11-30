n = int(input())
price = 0
result = []

for _ in range(n):
  a = list(map(int,input().split()))
  if a[0] == a[1] == a[2]:
    price = 10000+(a[0] * 1000)
    result.append(price)
  elif a[0] == a[1] != a[2] or a[0] == a[2] != a[1]:
    price = 1000 + (a[0] * 100)
    result.append(price)
  elif a[1] == a[2] != a[0]:
    price = 1000 + (a[1] * 100)
    result.append(price)
  else:
    price = max(a) *100
    result.append(price)
print(max(result)) 