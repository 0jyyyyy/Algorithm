n1 = int(input())
n2 = int(input())

n2_1 = n2 % 10 #5 
n2_2 = ((n2-n2_1) % 100) // 10 # 8
n2_3 = (n2-n2_1) // 100 # 3

print(n1 * n2_1)
print(n1 * n2_2)
print(n1 * n2_3)
print(n1 * n2)