import sys

t = int(sys.stdin.readline())

for _ in range(t):
  sys.stdin.readline()
  n = int(sys.stdin.readline())
  result = 0

  for _ in range(n):
    result += int(sys.stdin.readline())
  if result % n == 0 :
    print('YES')
  else:
    print('NO')