a,b = map(int,input().split())

c = int(input())

sum_ab = a + b

if sum_ab < (c*2):
  print(sum_ab)
else:
  print(sum_ab-(c*2))