n = int(input())

a,b = map(int, input().split())

m = (a // 2) + b

print(min(n, m))