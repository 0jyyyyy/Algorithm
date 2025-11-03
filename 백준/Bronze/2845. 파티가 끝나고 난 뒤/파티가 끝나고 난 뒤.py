L,P = map(int, input().split())
N = list(map(int,input().split()))

party = L*P

for i in N :
  i -= party
  print(i,end=' ')