K,N = map(int, input().split())
if N == 1:
  print(-1)
else:
  try:
    result = (K*N)//(N-1)
    if (K*N) % (N-1) : 
      result +=1
  except ZeroDivisionError:
    result = 0    
  print(result)