while True:
  num = 0
  num_list = []
  result = 1
  n = int(input())
  if n == 0:
    break
  for i in range(len(str(n))):
    num_list.append(str(n)[i])

  for j in num_list:
    if j == "0":
      num = 5
      result += num
    elif j == "1":
      num = 3
      result += num
    else:
      num = 4
      result += num

  print(result)