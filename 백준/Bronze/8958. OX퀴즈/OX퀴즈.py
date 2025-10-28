T = int(input())

sum_num_list = []
for _ in range(T):

  o_x_list = []
  str_num = 0
  end_num = 1
  flag = True

  num = 0
  sum_num = 0

  o_x = input()

  while flag:
    o_x_list.append(o_x[str_num:end_num])
    str_num += 1
    end_num += 1
    if end_num > len(o_x):
      flag = False

  for i in range(len(o_x_list)):
    if o_x_list[i] == "O":
      num +=1
      sum_num +=num  
    elif o_x_list[i] =="X":
      num = 0
  sum_num_list.append(sum_num)

for k in sum_num_list:
  print(k)