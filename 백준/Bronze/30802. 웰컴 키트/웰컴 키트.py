import math
n = int(input())

s = list(map(int,input().split()))

t,p = map(int,input().split())

count = 0

for i in s:
 count += math.ceil(i / t)

print(count)
print(n//p , n%p)