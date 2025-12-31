n = int(input())
lst = []
subject = {
  'Algorithm' : '204',
  'DataAnalysis': '207',
  'ArtificialIntelligence': '302',
  'CyberSecurity': 'B101',
  'Network': '303',
  'Startup': '501',
  'TestStrategy': '105'
}

for _ in range(n):
  m = input()
  lst.append(subject[m])

for i in lst:
  print(i)