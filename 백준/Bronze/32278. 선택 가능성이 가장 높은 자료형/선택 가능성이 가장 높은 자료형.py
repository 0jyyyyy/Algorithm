n = int(input())

if n <= (2**15)-1 and n >= -(2**15):
  print('short')
elif n <= (2**31)-1 and n >= -(2**31):
  print('int')
elif n <= (2**63)-1 and n >= -(2**63):
  print('long long')