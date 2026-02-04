n = int(input())
sum_1 = 0
sum_2 = 0
sum_3 = 0

for i in range(1,n+1):
  sum_1 += i
  sum_2 = sum_1 **2
  sum_3 += (i ** 3)
print(sum_1)
print(sum_2)
print(sum_3)