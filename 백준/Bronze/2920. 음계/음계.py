nums = list(map(int, input().split())) # 바로 리스트로 만들기
num =""

for i in nums:
  num += str(i)
  if num =="12345678":
    result = "ascending"
  elif num =="87654321":
    result = "descending"
  else:
    result = "mixed"
print(result)