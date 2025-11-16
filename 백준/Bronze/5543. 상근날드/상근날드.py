burger_list = []
total_list = []
for _ in range(3):
  burger = int(input())
  burger_list.append(burger)

coke = int(input())
cider = int(input())

for i in burger_list:
  total_list.append(i+coke)
  total_list.append(i+cider)
print(min(total_list)-50)
