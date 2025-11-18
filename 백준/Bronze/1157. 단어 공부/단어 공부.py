n = list(input().upper())
counter = {}
# 딕셔너리 형태로 값들을 저장
for i in n:
  try: counter[i] +=1
  except: counter[i]=1

# 딕셔너리 값중 최대 밸류값찾기
max_value = max(counter.values())
# 리스트 컴프리헨션으로 최대 밸류값의 키값을 찾기
result = [k for k, v in counter.items() if v == max_value]

if len(result) > 1:
  print("?")
else:
  print(result[0])