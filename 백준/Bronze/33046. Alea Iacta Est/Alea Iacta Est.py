a,b = map(int, input().split())
c,d = map(int, input().split())

gadong = []
jindong = []
for i in range(1, (a+b)+1):
    if i > 4:
        i -=4*((i//4))
        gadong.append(i)
    else:
        gadong.append(i)  

for k in range(gadong[-1],(c+d)+gadong[-1]):
    if k % 4 == 0:
      k = (k % 4) +4  
    if k > 4:
      k =k-4*((k//4))
      jindong.append(k)
    else:
        jindong.append(k)
print(jindong[-1])