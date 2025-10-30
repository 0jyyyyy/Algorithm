flag = True
while flag:
  n,m = map(int, input().split())
  if n != 0 and m != 0:
    if n > m : 
      print("Yes")
    else:
      print("No")
  else:
    flag = False