while True:
  n = input().lower()
  if n == "#":
    break
  start_num = 0
  end_num = 1
  n_list = []

  while True:
    n_list.append(n[start_num:end_num])
    start_num +=1
    end_num +=1
    if end_num > len(n):
      break
  
  count = 0

  for i in n_list:
    if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
      count += 1
  print(count)  