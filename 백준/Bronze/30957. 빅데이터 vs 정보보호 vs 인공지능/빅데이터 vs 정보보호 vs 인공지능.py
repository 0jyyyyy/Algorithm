n = int(input())

m = input()
lst = []
lst.append(m.count('S'))
lst.append(m.count('B'))
lst.append(m.count('A'))

if max(lst) == lst[0] and max(lst) == lst[1] and max(lst) == lst[2]:
  print('SCU')
elif max(lst) == lst[0] and max(lst) == lst[1]:
  print('BS')
elif max(lst) == lst[1] and max(lst) == lst[2]:
  print('BA')
elif max(lst) == lst[0] and max(lst) == lst[2]:
  print('SA')
elif max(lst) == lst[0]:
  print('S')
elif max(lst) == lst[1]:
  print('B')
elif max(lst) == lst[2]:
  print('A')