n = int(input())

all_lst = input().split()
used_lst = input().split()

for i in all_lst:
  if i not in used_lst:
    print(i)
    break