lst = []

for _ in range(7):
  a,b = input().split()
  lst.append([a, int(b)])

print(max(lst, key=lambda x: x[1])[0]) 