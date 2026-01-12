import math
import sys
flag = True
while flag:
  n = int(sys.stdin.readline())
  if n == 0:
    flag = False
    break
  lst = [int(i) for i in str(n)]

  total= 0
  lens = len(lst)
  for i,ls in enumerate(lst):
    # i는 순서, multi는 곱할수
    # 즉, 리스트의 길이에서 i를 뺀만큼 곱하기
    multi = lens - i
    total += ls*(math.factorial(multi))
  print(total) 