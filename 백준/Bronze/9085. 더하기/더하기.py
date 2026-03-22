t = int(input())

result = []
for _ in range(t):
  n = int(input())
  k = list(map(int, input().split()))
  total = sum(k)
  result.append(total)

for i in result:
  print(i)