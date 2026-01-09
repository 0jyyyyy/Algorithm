result_1 = []

for _ in range(4):
  result_1.append(int(input()))

result_2 = []
for _ in range(2):
  result_2.append(int(input()))

result_1.sort(reverse=True)
result_2.sort(reverse=True)

total = sum(result_1[:3]) + result_2[0]

print(total)