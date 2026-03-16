n = int(input())
results = []
for _ in range(n):
  a, b = map(str, input().split())

  sum_num = int(a,2) + int(b,2)

  result = bin(sum_num)[2:]
  results.append(result)

for i in results:
  print(i)