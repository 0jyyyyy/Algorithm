N,M = map(int, input().split())
basket = []
for a in range(N):
  basket.append(0)

for b in range(M):
  i,j,k = map(int, input().split())
  for c in range(i,j+1):
    basket[c-1] = k
result = (" ".join(map(str,basket)))
print(result)