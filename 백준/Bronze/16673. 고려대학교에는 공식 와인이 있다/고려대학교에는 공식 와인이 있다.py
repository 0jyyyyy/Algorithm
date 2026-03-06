c, k, p = map(int, input().split())

total = 0

for i in range(1, c+1):
  m = (k*i) + (p*(i**2))
  total += m
print(total)