t = int(input())
result = []

for _ in range(t):
  n = int(input())
  p1_score = 0
  p2_score = 0
  for _ in range(n):
    p1, p2 = input().split()
    if p1 == 'R' and p2 == 'S':
      p1_score += 1
    elif p1 == 'R' and p2 == 'P':
      p2_score += 1
    elif p1 == 'S' and p2 == 'P':
      p1_score += 1
    elif p1 == 'S' and p2 == 'R':
      p2_score += 1
    elif p1 == 'P' and p2 == 'R':
      p1_score += 1
    elif p1 == 'P' and p2 == 'S':
      p2_score += 1
    else:
      continue
  if p1_score > p2_score :
    result.append('Player 1')
  elif p1_score < p2_score :
    result.append('Player 2')
  else:
    result.append('TIE')

for i in result:
  print(i)