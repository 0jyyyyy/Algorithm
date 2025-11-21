A,B,C = map(int,input().split())

a_move = abs(A-B)-1
b_move = abs(B-C)-1

if a_move > b_move:
  print(a_move)
else:
  print(b_move)