t = int(input())

for _ in range(t):
  n = int(input())

  res = 0

  for i in range(1, n + 1):
    tri = (i + 1) * (i + 2) // 2

    res += i * tri
  print(res)