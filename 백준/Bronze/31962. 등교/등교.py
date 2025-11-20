N,X = map(int, input().split())
result = []

for _ in range(N):
  S,T = map(int,input().split())
  st = S+T
  if st <= X:
    result.append(S)

if len(result) == 0:
  print(-1)
else:
  print(max(result))