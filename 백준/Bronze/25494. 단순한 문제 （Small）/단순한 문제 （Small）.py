t = int(input())
for _ in range(t):
    result = 0
    a,b,c = map(int, input().split())
    for x in range(1, a+1):
        for y in range(1,b+1):
            for z in range(1,c+1):
                if ((x % y) == (y % z)) and ((y % z) == (z % x)) and ((z % x) == (x % y)):
                    result += 1
    print(result) 