N,X = map(int, input().split())
s_ls = []
t_ls = []

for _ in range(N):
  S,T = map(int,input().split())
  s_ls.append(S)
  t_ls.append(T)
  
result = min(s_ls) + min(t_ls)
if result <= X:
  print(max(s_ls))
else:
  print(-1)