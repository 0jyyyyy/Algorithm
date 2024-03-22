years = int(input())
yun_years = 0
if years % 4 == 0 and years % 100 != 0 or years % 400 == 0:
  yun_years = 1
  print(yun_years)
else:
  print(yun_years)
