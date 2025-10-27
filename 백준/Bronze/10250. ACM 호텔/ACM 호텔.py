num = int(input())
for i in range(num):
  H,W,N = map(int, input().split())
  floor = N % H #층수
  room = N // H +1 # 호수
  if floor == 0:
     room -= 1
     floor = H
  print(floor*100 + room)
