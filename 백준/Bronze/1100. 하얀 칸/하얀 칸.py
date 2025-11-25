count = 0
for i in range(1,9):
  a = input()
  if i % 2 == 0:
    count += a[1::2].count("F")
  else:
    count += a[0::2].count("F")
print(count)