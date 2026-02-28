n = int(input())

m = list(map(int, input().split()))

result = []

for i in m:
  if i >= 300 :
    result.append(1)
  elif i < 300 and i >=275 :
    result.append(2)
  elif i < 275 and i >=250 :
    result.append(3)
  else:
    result.append(4)

print(' '.join(map(str, result)))