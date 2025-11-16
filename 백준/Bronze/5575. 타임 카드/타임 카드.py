time_list = []

for _ in range(3):
  a = list(map(int, input().split()))
  hour = a[3] - a[0]
  min = (a[4] - a[1]) % 60
  if a[1] > a[4]:
    hour -= 1
  second = (a[5] - a[2]) % 60
  if a[2] > a[5]:
    min -= 1  
    if min < 0 :
      min += 60
      hour -= 1
  
  time_list.append(f"{hour} {min} {second}")
for i in time_list:
  print(i)