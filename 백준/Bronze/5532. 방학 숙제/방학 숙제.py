import math

L = int(input())
A = int(input())
B = int(input())
C = int(input())
D = int(input())

result_1 = math.ceil(A / C)
result_2 = math.ceil(B / D)

if result_1 > result_2 :
  result_2 = result_1
else:
  result_1 = result_2

result = L - result_1

print(result)