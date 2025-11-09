jin_mbti = input()
N = int(input())
mbti_list = []
result = 0

for _ in range(N):
  mbti_list.append(input())

for i in mbti_list:
  if jin_mbti == i:
    result +=1
print(result)