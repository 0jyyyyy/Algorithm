a,b = map(int, input().split())
while True:
  b = b + a
  if b >= 5 :
    print('yt')
    break
  a = a + b
  if a >= 5:
    print('yj')
    break