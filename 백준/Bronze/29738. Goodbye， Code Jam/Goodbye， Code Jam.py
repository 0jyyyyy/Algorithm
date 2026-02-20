t = int(input())
for i in range(t):
  n = int(input())

  if n > 4500:
    print(f'Case #{i+1}: Round 1')
  elif n <= 4500 and n > 1000:
    print(f'Case #{i+1}: Round 2')
  elif n <= 1000 and n > 25:
    print(f'Case #{i+1}: Round 3')
  else:
    print(f'Case #{i+1}: World Finals') 