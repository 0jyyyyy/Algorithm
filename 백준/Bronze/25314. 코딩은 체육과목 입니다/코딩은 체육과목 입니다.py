N = int(input())
long_times = 0 
for i in range(N//4):
  if N % 4 == 0:
    long_times += 1

print(("long " * long_times) + "int")