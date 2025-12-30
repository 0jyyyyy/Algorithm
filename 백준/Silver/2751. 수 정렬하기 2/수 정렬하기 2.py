import sys

n = int(sys.stdin.readline())

lst = []

for _ in range(n):
  m = int(sys.stdin.readline())
  lst.append(m)

lst.sort()

for i in lst:
  print(i)