import sys

n = int(sys.stdin.readline())
sum  = 0
for i in range(n):
  con = int(sys.stdin.readline())
  sum += con
print(sum-(n-1))