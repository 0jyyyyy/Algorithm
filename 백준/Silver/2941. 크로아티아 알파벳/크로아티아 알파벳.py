alpa = ["c=","c-","dz=","d-","lj","nj","s=","z="]

n = input()

for i in range(len(alpa)):
  if alpa[i] in n:
    n = n.replace(alpa[i],"*")
print(len(n))