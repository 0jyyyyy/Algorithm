n, m = map(int, input().split())

total_count = n

while n >= m:
    n //= m
    total_count += n

print(total_count)