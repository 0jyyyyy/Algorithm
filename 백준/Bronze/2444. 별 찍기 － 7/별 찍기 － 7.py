n = int(input())

emp_1 = 1
star_1 = 1

emp_2 = 0
star_2 = 1
for _ in range(n-1):
  print(" " * (n-emp_1) + "*" * star_1)
  emp_1 += 1
  star_1 += 2


for _ in range(n):
  print(" " * emp_2 + "*" * ((2*n)-star_2))
  emp_2 += 1
  star_2 += 2