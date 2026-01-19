n = int(input())

row = n // 2
col = n - row
# 가로로 자른거 +1 곱하기 세로로 자른거 +1
print((row+1) * (col+1))