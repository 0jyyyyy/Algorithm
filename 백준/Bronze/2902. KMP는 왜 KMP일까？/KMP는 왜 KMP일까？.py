n = input()
res = n.split('-')

answer = '' 
for i in res:
  answer += i[0]
print(answer)