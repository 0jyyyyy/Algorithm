A = int(input())
B = int(input())
C = int(input())

x = A * B * C

lis = []

str_num = 0
end_num = 1
flag = True

while flag:
  lis.append(str(x)[str_num:end_num])
  str_num += 1
  end_num += 1
  if end_num > len(str(x)):
    flag = False

for i in range(10):
  print(lis.count(f'{i}'))    
  