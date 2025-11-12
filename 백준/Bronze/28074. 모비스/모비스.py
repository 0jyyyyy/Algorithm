mobis = ["M","O","B","I","S"]

n = input()

result = "YES"

for i in mobis:
  if i not in n:
    result = "NO"
    break

print(result)