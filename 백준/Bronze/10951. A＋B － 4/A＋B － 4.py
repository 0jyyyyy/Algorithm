import sys
flag = True
while flag:
  try:
    A,B =map(int, sys.stdin.readline().split())
    print(A+B)
  except:
    flag = False