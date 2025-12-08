from collections import Counter
n = int(input())
names = []
sur_name=[]
for _ in range(n):
  name = input()
  names.append(name)

for i in names:
  sur_name.append(i[0])

count_result = Counter(sur_name)
five_more = [
    item 
    for item, count in count_result.items() 
    if count >= 5  
]
if five_more :
  print(''.join(sorted(five_more)))
else:
  print('PREDAJA')  