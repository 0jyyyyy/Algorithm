n = int(input())
m = n
count = 0
while True:
  if n < 10:
    n_ls = ['0' , f'{n}']
  else:
    n_ls = list(str(n))
  n_sum = int(n_ls[0]) + int(n_ls[1])
  if n_sum < 10:
    n_sum_ls = ['0', f'{n_sum}']
  else:
    n_sum_ls = list(str(n_sum))
  n_result = n_ls[1] + n_sum_ls[1]
  count += 1
  n = int(n_result)
  if int(n_result) == m:
    print(count)
    break