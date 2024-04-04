N,M = map(int, input().split())
N_list = []
for a in range(1, N+1):
  N_list.append(a)
for b in range(M):
   opt = 0
   i,j = map(int,input().split())
   opt = N_list[i-1]
   N_list[i-1] = N_list[j-1]
   N_list[j-1] = opt
result = (" ".join(map(str,N_list)))
print(result)