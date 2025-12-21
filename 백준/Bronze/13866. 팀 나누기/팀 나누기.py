n = list(map(int,input().split()))

m = []
m.append(max(n))
n.remove(max(n))

m.append(min(n))
n.remove(min(n))

print(abs((m[0] + m[1]) - (n[0] + n[1])))