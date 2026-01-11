n = int(input())

lst = list(map(int, input().split()))

result = 0
upset = 0

for i in lst:
  if i == 1:
    upset +=1
  else:
    upset -= 1
  result += upset
print(result)