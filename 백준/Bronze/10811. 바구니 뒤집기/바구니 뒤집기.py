N,M = map(int, input().split())

num_list =[]
for a in range(1,N+1):
    num_list.append(a)
for _ in range(M):
    i,j = map(int, input().split())
    num_list[i-1:j] = num_list[i-1:j][::-1]
    
for k in num_list:
    print(k,end=" ")