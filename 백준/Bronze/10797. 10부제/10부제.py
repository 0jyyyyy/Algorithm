n = int(input())
cars = list(map(int,input().split()))
count = 0
for i in cars:
  if i == n:
    count +=1
print(count)