import math

n = int(input())
n_list = list(map(int, input().split()))
result = 0

for i in n_list:
  if i < 2 :
    continue

  for j in range(2, int(math.sqrt(i)+1)):
    if i % j == 0:
      break
  else:
    result += 1
print(result)