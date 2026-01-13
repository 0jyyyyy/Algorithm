s = input()

if s == ')1(':
  print(2)
elif s == '(1)':
  print(0)
else: # 나머지 경우는 모두 한번만 움직이면 된다.
  print(1)