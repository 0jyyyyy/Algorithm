n, q = map(int,input().split())

sum_i = 0
t = []

# 1단계 누적길이 리스트 t
for i in range(n):
  b = int(input())
  sum_i += b
  t.append(sum_i)
# 2단계 Q개 질문 처리
for _ in range(q):
  t_list = int(input())
  for j in range(n):
    if t_list < t[j]:
      print(j + 1)
      break