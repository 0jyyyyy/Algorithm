lst = []
sum_lst = 0
for _ in range(7):
  n = int(input())
  if n % 2 != 0:
    lst.append(n)

for i in lst:
  sum_lst += i

if len(lst) == 0:
  print(-1)
else:
  print(sum_lst)
  print(min(lst))