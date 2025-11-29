n = int(input())

ls = list(input())
convert_ls = []

for i in ls:
  if i == 'I':
    convert_ls.append('i')
  elif i == 'l':
    convert_ls.append('L')
print("".join(convert_ls))