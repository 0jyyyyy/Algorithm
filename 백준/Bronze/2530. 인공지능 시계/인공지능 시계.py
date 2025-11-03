A,B,C = map(int, input().split()) 
D = int(input())

C = C + D

if C > 59 :
  C_div = C // 60
  B = B + C_div
  C = C % 60
if B > 59 :
  B_div = B // 60
  A = A + B_div
  B = B % 60

A %= 24

print(f"{A} {B} {C}")