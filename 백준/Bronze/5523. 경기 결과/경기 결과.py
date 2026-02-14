n = int(input())
a_win = 0
b_win = 0
for _ in range(n):
  a,b = map(int, input().split())
  if a > b:
    a_win += 1
  elif a < b:
    b_win += 1
print(f'{a_win} {b_win}')