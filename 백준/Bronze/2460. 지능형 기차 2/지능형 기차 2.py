total = 0
tot_list = []
for _ in range(10):
  o,i = map(int, input().split())
  total += i-o
  tot_list.append(total)
print(max(tot_list))