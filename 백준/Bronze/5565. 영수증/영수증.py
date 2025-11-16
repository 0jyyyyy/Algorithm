total_price = int(input())
book_price = 0
for _ in range(9):
  price = int(input())
  book_price += price
print(total_price - book_price)