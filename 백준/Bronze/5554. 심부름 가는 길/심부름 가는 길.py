result = 0

for _ in range(4):
  time = int(input())
  result += time

x = result //60
y= result % 60

print(x)
print(y)