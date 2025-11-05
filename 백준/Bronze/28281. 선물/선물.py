n,x = map(int, input().split())
socks = []

price = list(map(int,input().split()))

if len(price) != n :
  print("리스트의 길이가 옳지않아 종료")
  exit()

for i in range(n-1):
  socks.append(price[i]*x + price[i+1]*x)
print(min(socks))  