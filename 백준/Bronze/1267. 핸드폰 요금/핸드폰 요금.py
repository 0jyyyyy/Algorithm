import math

n = int(input())
n_list = list(map(int, input().split()))
M = 0
Y = 0
for i in n_list:
  y = (math.ceil(i//30)+1) * 10
  m = (math.ceil(i//60)+1) * 15
  M += m
  Y += y

if M < Y:
  print(f"M {M}")
elif M == Y:
  print(f"Y M {M}")
else:
  print(f"Y {Y}")