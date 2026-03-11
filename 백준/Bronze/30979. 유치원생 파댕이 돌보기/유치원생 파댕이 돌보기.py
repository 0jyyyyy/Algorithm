t = int(input())

n = int(input())

c = list(map(int, input().split()))

f = sum(c)

if f >= t:
  print('Padaeng_i Happy')
else:
  print('Padaeng_i Cry')