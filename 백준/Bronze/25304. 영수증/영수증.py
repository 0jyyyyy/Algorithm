Total_price = int(input())
Type = int(input())
Sum_price = 0
for i in range(Type):
  price,product = map(int, input().split())
  Sum_price += price*product
if Total_price == Sum_price :
  print("Yes")
else:
  print("No")