a,b,c = map(int, input().split())

result_1 = (a * b) / c
result_2 = (a / b) * c

print(int(max(result_1,result_2)))