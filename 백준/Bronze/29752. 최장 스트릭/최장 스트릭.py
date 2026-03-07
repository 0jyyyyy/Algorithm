n = int(input())

result = list(map(int, input().split()))

max_str = 0
cur_str = 0

for i in result:
  if i > 0:
    cur_str +=1
    if cur_str > max_str:
      max_str = cur_str
  else:
    cur_str = 0
print(max_str)