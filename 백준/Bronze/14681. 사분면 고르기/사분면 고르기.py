x = int(input())
y = int(input())
n = 0
if x > 0 and y > 0 :
  n = 1
elif x > 0 and y < 0 :
  n = 4
elif x < 0 and y < 0 :
  n = 3
else : 
  n = 2
print(n)