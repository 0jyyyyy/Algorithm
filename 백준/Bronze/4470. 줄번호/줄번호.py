n = int(input())
name_list=[]
for _ in range(n):
  name = input()
  name_list.append(name)

for i in range(len(name_list)):
  print(f"{i+1}. {name_list[i]}")