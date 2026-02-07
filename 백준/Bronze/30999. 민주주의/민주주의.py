n,m = map(int,input().split())
result = 0

for _ in range(n):
  i = input()
  if i.count('O') > m //2 :
    result += 1
print(result)