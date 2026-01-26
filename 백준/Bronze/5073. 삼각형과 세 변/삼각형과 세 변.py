flag = True
while flag:
  a,b,c = map(int, input().split())
  if a == 0 and b == 0 and c == 0:
    flag = False
    break
  if a == b == c :
    print('Equilateral')
  elif a == b != c or a == c != b or b == c != a :
    if a+b <= c or a+c <=b or b+c <=a:
      print('Invalid')
    else:
      print('Isosceles')
  else:
    if a+b <= c or a+c <=b or b+c <=a:
      print('Invalid')
    else:
      print('Scalene')