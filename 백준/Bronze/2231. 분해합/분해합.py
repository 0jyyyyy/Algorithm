n = int(input())

result = 0

for i in range(1, n+1):
  n_list = list(map(int, str(i)))
  result = sum(n_list) + i
  if result == n:
    print(i)
    break
  if i == n:
    print(0)