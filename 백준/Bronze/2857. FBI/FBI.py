fbi_lst = []

for i in range(1,6):
  fbi = input()
  if 'FBI' in fbi:
    fbi_lst.append(i)
if len(fbi_lst) > 0:
  for i in fbi_lst:
    print(i , end=' ')
else:
  print('HE GOT AWAY!')