n, m = map(int, input().split())

ls = []
for i in range(m):
  nu = list(map(int,input().split()))
  ls.extend(nu)
  
for i in range(1,n+1):
  print(ls.count(i))