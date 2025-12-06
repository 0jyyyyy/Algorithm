n,m = map(int,input().split())

a = 100 - n
b = 100 - m
c = 100 - (a+b)
d = a*b
q = a*b // 100
r = a*b % 100

print(f'{a} {b} {c} {d} {q} {r}')
print(f'{c+q} {r}')