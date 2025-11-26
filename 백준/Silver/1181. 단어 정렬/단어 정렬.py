n = int(input())
word = []
for _ in range(n):
  word.append(input())
words = sorted(set(word),key=lambda x:(len(x),x))

for i in words:
  print(i)