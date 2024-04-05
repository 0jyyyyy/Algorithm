N_list = []
result= []
opt = 0
for i in range(1,31):
  N_list.append(i)
for k in range(28):  
  N = int(input())
  result.append(N)
final = list(set(N_list) - set(result))
for j in range(len(final)):
  if final[j-1] > final[j]:
    opt = final[j-1]
    final[j-1] = final[j]
    final[j] = opt
print(final[0])
print(final[1])