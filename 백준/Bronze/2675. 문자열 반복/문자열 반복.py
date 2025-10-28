S = int(input())

result_list = []
for _ in range(S):  
  result = ""
  R,P = map(str, input().split())
  for i in P:
    result += i*int(R)
  result_list.append(result)

for k in result_list:
  print(k)