num_list = []
diff_num = 0

for i in range(10):
  num = int(input())
  num_list.append(num % 42)

num_list.sort()
for i in range(9):
  if num_list[i] != num_list[i+1]:
      diff_num += 1
print(diff_num + 1) 