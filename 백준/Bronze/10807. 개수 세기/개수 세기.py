N = int(input())
Ns =list(map(int, input().split(" ")))
v = int(input())
find_v = 0
for i in Ns:
  if i == v :
    find_v +=1
print(find_v)