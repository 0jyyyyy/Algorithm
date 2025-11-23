n = int(input())
cups = [1,2,3]

for _ in range(n):
  a,b = map(int, input().split())
  index_a = cups.index(a)
  index_b = cups.index(b)
  # 몇번째 인덱스인지 확인
  # print(index_a)
  # print(index_b)
  # 그 인덱스에 값을 반대로 저장
  cups[index_a] = b
  cups[index_b] = a
  # print(cups)
print(cups[0])