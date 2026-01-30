n = int(input())
for _ in range(n):
  name = list(map(str, input().split()))
  name[0] = 'god'
  print(''.join(name))