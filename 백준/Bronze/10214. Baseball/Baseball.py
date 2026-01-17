t = int(input())

for _ in range(t):
  y_result = 0
  k_result = 0
  for _ in range(9):
    y,k = map(int,input().split())
    y_result += y
    k_result += k
  if y_result > k_result:
    print('Yonsei')
  elif y_result < k_result:
    print('Korea')
  else:
    print('Draw')  
