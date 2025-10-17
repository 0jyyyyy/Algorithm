num = int(input())
slice_words = [] 


for i in range(num):
  word = input()
  slice_words.append((word[0]+word[-1]))

for k in slice_words:
  print(k)