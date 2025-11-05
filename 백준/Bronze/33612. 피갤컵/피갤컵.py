N = int(input())
year = 2024
month = 1

month += N*7
mon = month // 13
year += mon
month %= 12
if month % 12 == 0:
  month = 12
print(year, month, end=" ")