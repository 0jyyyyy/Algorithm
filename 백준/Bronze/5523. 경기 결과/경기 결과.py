import sys

n = int(sys.stdin.readline())
a_win = 0
b_win = 0
for _ in range(n):
  a,b = map(int, sys.stdin.readline().split())
  if a > b:
    a_win += 1
  elif a < b:
    b_win += 1
print(a_win, b_win)