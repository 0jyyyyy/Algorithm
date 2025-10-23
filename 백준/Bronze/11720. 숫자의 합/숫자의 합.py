
a = input()
b = input()

lis = []
str_num = 0
end_num = 1

flag = True

while flag :
  lis.append(b[str_num:end_num])
  str_num +=1
  end_num +=1
  if end_num > len(b):
    flag = False

total_sum = 0
for i in lis:
  total_sum += int(i)
print(total_sum)