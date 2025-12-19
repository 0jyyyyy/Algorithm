import math

n,m = map(int, input().split())

gcd_result = math.gcd(n,m)
lcm_result = math.lcm(n,m)

print(gcd_result)
print(lcm_result)